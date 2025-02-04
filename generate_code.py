import os
import subprocess
import datetime
import time
import re
from langchain_ollama import OllamaLLM
import argparse
import random
import sys


# Parser des arguments
parser = argparse.ArgumentParser(description='Générer ou modifier un script Python avec Ollama')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-g', '--generate', action='store_true', help='Générer un script Python')
group.add_argument('-f', '--fix', action='store_true', help='Réparer un script Python existant')
group.add_argument('-d', '--doc', action='store_true', help='Générer de la documentation pour un script')

args = parser.parse_args()

# Vérifier que exactement une option est sélectionnée
if sum([args.generate, args.fix, args.doc]) != 1:
    print("❌ Veuillez choisir une seule option parmi -g, -f et -d.")
    sys.exit(1)

# Debug : Afficher l'option choisie
if args.generate:
    print("[✔] Mode génération de script activé.")
elif args.fix:
    print("[✔] Mode correction de script activé.")
elif args.doc:
    print("[✔] Mode documentation activé.")

generate = args.generate
fix = args.fix
doc = args.doc


# Dossier du repo
repo_path = "/home/melissa/Documents/automat-gh/AUTO"

# Vérifier si le modèle deepseek est déjà téléchargé
print("[⏳] Vérification du modèle 'deepseek-r1'...")
subprocess.run(["ollama", "pull", "deepseek-r1"])

# Attendre quelques secondes pour s'assurer que le modèle est bien disponible
time.sleep(2)

# Serve model 
print("[⏳] Démarrage du serveur Ollama...")
subprocess.Popen(["ollama", "serve", "deepseek-r1"])
print("[✔] Modèle 'deepseek' prêt !")

if generate :
    commit_message = "[ADD] "
    # Demander à Ollama de générer un script Python utile
    prompt = """Génère un script Python fonctionnel et intéressant pour un problème algorithmique complexe de ton choix. N'ajoute aucun commentaire dans le script. Et n'ajoute pas de texte superflue en dehors du script Python.
    Retourne uniquement la réponse sous ce format exact :

    Nom du fichier : $$$<nom_du_script_sans_extension>$$$
    Code :
    <contenu_du_script>
    """
    
else:
    # Ouvrir un script Python aléatoire dans le dossier "generated"
    generated_files = os.listdir(os.path.join(repo_path, "generated"))
    if len(generated_files) == 0:
        print("[❌] Aucun fichier généré trouvé.")
        sys.exit(1)
    else:
        print("[⏳] Ouverture d'un fichier généré...")
        nb_file = len(generated_files)
        random_file = random.randint(0, nb_file-1)
        file_path = os.path.join(repo_path, "generated", generated_files[random_file])
        file_name = os.path.basename(file_path)
        with open(file_path, "r") as f:
            script_content = f.read()
        print("[✔] Fichier ouvert.")
        if doc:
            commit_message = "[DOC] "
            prompt = f"""Génère de la documentation Markdown pour le script Python suivant, renvoie le code au complet sans ajouter de commentaire et de texte superflue en dehors du script Python:
            {script_content}
            """
            file_name = file_name.replace(".py", ".md")
            file_path = os.path.join(repo_path, "generated", file_name)
        elif fix:
            commit_message = "[FIX] "
            prompt = f"""Répare le script Python suivant, renvoie le code au complet sans ajouter de commentaire et de texte superflue en dehors du script Python:
            {script_content}
        """

llm = OllamaLLM(model="deepseek-r1")
def get_script_content(prompt):
    print("[⏳] Génération du script Python...")

    response = llm.invoke(prompt)

    return response

code_response = get_script_content(prompt)

while True:
    # Extraction du nom du fichier et du contenu du script
    try:
        if generate:
            # Utilisation d'une expression régulière pour extraire le contenu entre ```python et ```
            script_content_match = re.search(r'```python(.*?)```', code_response, re.DOTALL)
        else:
            # Utilisation d'une expression régulière pour extraire le contenu entre ```md et ```
            script_content_match = re.search(r'```md(.*?)```', code_response, re.DOTALL)
            
        if script_content_match:
            script_content = script_content_match.group(1).strip()
            print("[✔] Contenu du script trouvé.")
            break
        else:
            print("[❌] Erreur : Contenu du script non trouvé.")
            print(code_response)
            r = input("Appuyez sur Entrée pour quitter ou R pour réessayer...")
            if r.lower() == "r":
                code_response = get_script_content(prompt)
            else:
                exit()
    except Exception as e:
        print(f"[❌] Erreur : {e}\nContenu du script non trouvé.")
        print(code_response)
        r = input("Appuyez sur Entrée pour quitter ou R pour réessayer...")
        if r.lower() == "r":
            code_response = get_script_content(prompt)
        else:
            exit()

if generate :
    try :
        file_name_line =  re.search(r'\$\$\$(.*?)\$\$\$', code_response).group(1)
        # Nettoyage du nom du fichier
        script_name = file_name_line.replace(" ", "_").replace("-", "_")
    except Exception as e:
        print(f"[❌] Erreur pour le nom du script : {e}")
        script_name = "script"
        
    # Ajout d'un timestamp pour éviter les conflits
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    file_name = f"generated/{script_name}_{timestamp}.py"
    file_path = os.path.join(repo_path, file_name)

# Écriture du fichier
with open(file_path, "w") as f:
    f.write(script_content)

print(f"[✔] Fichier créé : {file_path}")

# Git : ajouter, commit et push
subprocess.run(["git", "-C", repo_path, "add", "."])
subprocess.run(["git", "-C", repo_path, "commit", "-m", f"{commit_message}{file_name}"])
subprocess.run(["git", "-C", repo_path, "push", "origin", "main"])

print("[✔] Push terminé avec succès !")
import os
import subprocess
import datetime
import ollama
import time
import re
from langchain_ollama import OllamaLLM


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

llm = OllamaLLM(model="deepseek-r1")
def get_script_content():
    print("[⏳] Génération du script Python...")
    # Demander à Ollama de générer un script Python utile
    prompt = """Génère un script Python fonctionnel et intéressant pour un problème algorithmique complexe de ton choix. N'ajoute aucun commentaire dans le script. Et n'ajoute pas de texte superflue en dehors du script Python.
    Retourne uniquement la réponse sous ce format exact :

    Nom du fichier : $$$<nom_du_script_sans_extension>$$$
    Code :
    <contenu_du_script>
    """

    response = llm.invoke(prompt)

    code_response = response["message"]["content"]
    return code_response

code_response = get_script_content()

while True:
    # Extraction du nom du fichier et du contenu du script
    try:
        # Utilisation d'une expression régulière pour extraire le contenu entre ```python et ```
        script_content_match = re.search(r'```python(.*?)```', code_response, re.DOTALL)
        if script_content_match:
            script_content = script_content_match.group(1).strip()
            print("[✔] Contenu du script trouvé.")
            break
        else:
            print("[❌] Erreur : Contenu du script non trouvé.")
            print(code_response)
            r = input("Appuyez sur Entrée pour quitter ou R pour réessayer...")
            if r.lower() == "r":
                code_response = get_script_content()
            else:
                exit()
    except Exception as e:
        print(f"[❌] Erreur : {e}\nContenu du script non trouvé.")
        print(code_response)
        r = input("Appuyez sur Entrée pour quitter ou R pour réessayer...")
        if r.lower() == "r":
            code_response = get_script_content()
        else:
            exit()


try :
    file_name_line =  re.search(r'\$\$\$(.*?)\$\$\$', code_response).group(1)
    # Nettoyage du nom du fichier
    script_name = file_name_line.replace(" ", "_").replace("-", "_")
except Exception as e:
    print(f"[❌] Erreur : {e}")
    script_name = "script.py"
    
# Ajout d'un timestamp pour éviter les conflits
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"{script_name}_{timestamp}.py"
file_path = os.path.join(repo_path, file_name)

# Écriture du fichier
with open(file_path, "w") as f:
    f.write(script_content)

print(f"[✔] Fichier créé : {file_path}")

# Git : ajouter, commit et push
subprocess.run(["git", "-C", repo_path, "add", file_name])
subprocess.run(["git", "-C", repo_path, "commit", "-m", f"Ajout du fichier {file_name}"])
subprocess.run(["git", "-C", repo_path, "push", "origin", "main"])

print("[✔] Push terminé avec succès !")
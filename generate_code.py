import os
import subprocess
import time
import re
from langchain_ollama import OllamaLLM
import argparse
import random
import sys

# Constants
REPO_PATH = "/home/melissa/Documents/automat-gh/AUTO"
MODEL_NAME = "deepseek-r1"

# Argument Parser
def parse_arguments():
    parser = argparse.ArgumentParser(description='Générer ou modifier un script Python avec Ollama')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-g', '--generate', action='store_true', help='Générer un script Python')
    group.add_argument('-f', '--fix', action='store_true', help='Réparer un script Python existant')
    group.add_argument('-d', '--doc', action='store_true', help='Générer de la documentation pour un script')
    group.add_argument('-c', '--clean', action='store_true', help='Push pour le nettoyage du repo')
    group.add_argument('-u', '--update', action='store_true', help='Mettre à jour le modèle code de génération')
    return parser.parse_args()

# Git Operations
def git_operations(commit_message):
    subprocess.run(["git", "-C", REPO_PATH, "add", "."])
    subprocess.run(["git", "-C", REPO_PATH, "commit", "-m", commit_message])
    subprocess.run(["git", "-C", REPO_PATH, "push", "origin", "main"])
    print("[✔] Push terminé avec succès !")

# Show Code
def show_code(code_response):
    s = input("Voulez-vous voir le contenu généré par le modèle (Y/N) ")
    if s.lower() == 'y':
        print(code_response)

# Get Script Content
def get_script_content(prompt, llm, mode):
    print(f"[⏳] {mode} en cours...")
    response = llm.invoke(prompt)
    return response

# Main Function
def main():
    args = parse_arguments()

    if sum([args.generate, args.fix, args.doc, args.clean, args.update]) != 1:
        print("""❌ Veuillez choisir une seule option parmi :
              -g, --generate : Générer un script Python
              -f, --fix : Réparer un script Python existant
              -d, --doc : Générer de la documentation pour un script
              -c, --clean : Push pour le nettoyage du repo
              -u, --update : Mettre à jour le modèle code de génération""")
        sys.exit(1)

    if args.clean:
        git_operations("[CLEAN] Nettoyage des fichiers générés")
    elif args.update:
        subprocess.run(['git', '-C', REPO_PATH, 'pull'])
        git_operations("[UPDATE] Update code generation")
    else:
        subprocess.run(["ollama", "pull", MODEL_NAME])
        time.sleep(2)
        subprocess.Popen(["ollama", "serve", MODEL_NAME])
        print("[✔] Modèle 'deepseek' prêt !")

        llm = OllamaLLM(model=MODEL_NAME)
        if args.generate:
            prompt = """Génère un script Python fonctionnel et intéressant pour un problème algorithmique complexe de ton choix. N'ajoute aucun commentaire dans le script. Et n'ajoute pas de texte superflue en dehors du script Python.
            Retourne uniquement la réponse sous ce format exact :

            Nom du fichier : $$$<nom_du_script_sans_extension>$$$
            Code :
            <contenu_du_script>
            """
            mode = "Génération du script Python"
        else:
            generated_files = os.listdir(os.path.join(REPO_PATH, "generated"))
            generated_files = [file for file in generated_files if not file.endswith(".md")]
            if not generated_files:
                print("[❌] Aucun fichier généré trouvé.")
                sys.exit(1)

            random_file = random.choice(generated_files)
            file_path = os.path.join(REPO_PATH, "generated", random_file)
            with open(file_path, "r") as f:
                script_content = f.read()

            if args.doc:
                prompt = f"""Génère de la documentation Markdown pour le script Python suivant, renvoie le code au complet sans ajouter de commentaire et de texte superflue en dehors du script Python:
                {script_content}
                """
                mode = "Génération de la documentation"
                file_name = random_file.replace(".py", ".md")
            elif args.fix:
                prompt = f"""Répare le script Python suivant, renvoie le code au complet sans ajouter de commentaire et de texte superflue en dehors du script Python:
                {script_content}
                """
                mode = "Correction du script Python"
                file_name = random_file

        code_response = get_script_content(prompt, llm, mode)

        while True:
            try:
                if args.generate or args.fix:
                    script_content_match = re.search(r'```python(.*?)```', code_response, re.DOTALL)
                else:
                    script_content_match = re.search(r'```markdown(.*)```', code_response, re.DOTALL)

                if script_content_match:
                    script_content = script_content_match.group(1).strip()
                    print("[✔] Contenu du script trouvé.")
                    break
                else:
                    print("[❌] Erreur : Contenu du script non trouvé.")
                    show_code(code_response)
                    r = input("Appuyez sur Entrée pour quitter ou R pour réessayer...")
                    if r.lower() == "r":
                        code_response = get_script_content(prompt, llm, mode)
                    else:
                        exit()
            except Exception as e:
                print(f"[❌] Erreur : {e}\nContenu du script non trouvé.")
                show_code(code_response)
                r = input("Appuyez sur Entrée pour quitter ou R pour réessayer...")
                if r.lower() == "r":
                    code_response = get_script_content(prompt, llm, mode)
                else:
                    exit()

        if args.generate:
            try:
                file_name_line = re.search(r'\$\$\$(.*?)\$\$\$', code_response).group(1)
                script_name = file_name_line.replace(" ", "_").replace("-", "_")
            except Exception as e:
                print(f"[❌] Erreur pour le nom du script : {e}")
                show_code(code_response)
                script_name = input("Entrez le nom du script : ")
            file_name = f"generated/{script_name}.py"
            file_path = os.path.join(REPO_PATH, file_name)

        with open(file_path, "w") as f:
            f.write(script_content)

        print(f"[✔] Fichier créé : {file_path}")
        git_operations(f"{mode} {file_name}")

if __name__ == "__main__":
    main()

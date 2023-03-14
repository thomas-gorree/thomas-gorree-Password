import re
import hashlib
import json
import tinker as tk



def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Fonction pour enregistrer les mots de passe dans un fichier JSON
def save_passwords(passwords):
    with open('passwords.json', 'w') as f:
        json.dump(passwords, f)

# Fonction pour récupérer les mots de passe depuis un fichier JSON
def load_passwords():
    try:
        with open('passwords.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def principale():
    passwords = load_passwords()
    # la je demande se que je veux faire
    while True:
        print("Que voulez-vous faire ?")
        print("1. Ajouter un nouveau mot de passe")
        print("2. Afficher les mots de passe existants")
        print("3. Quitter")
        choice = input("> ")

        if choice == "1":
            while True:
                password = input("Mot de passe : ")
                if len(password) < 8 or len(password) > 40:
                    print("Le mot de passe doit contenir entre 8 et 40 caractères.")
                elif not re.search(r"[A-Z]", password):
                    print("Le mot de passe doit contenir au moins une lettre majuscule.")
                elif not re.search(r"[a-z]", password):
                    print("Le mot de passe doit contenir au moins une lettre minuscule.")
                elif not re.search(r"[0-9]", password):
                    print("Le mot de passe doit contenir au moins un chiffre.")
                elif not re.search(r"[!@#$%^&*]", password):
                    print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
                elif password in passwords:
                    print("Ce mot de passe a déjà été enregistré.")
                else:
                 hashed_password = hash_password(password)
                passwords[password] = {
                    "password": hashed_password
                }
                save_passwords(passwords)
                print("Le mot de passe a été enregistré avec succès !")
                break


        elif choice == "2":
            if len(passwords) == 0:
                print("Aucun mot de passe enregistré.")
            else:
                print("Voici la liste des mots de passe enregistrés :\n")
                for password, data in passwords.items():
                    print(f"-> Mot de passe crypté : {data['password']}")

        elif choice =="3":
            break

        else:
            print("Choix invalide.")
principale()
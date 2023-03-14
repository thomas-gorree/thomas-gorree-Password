import hashlib
import json

# Fonction pour hacher un mot de passe
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

# Fonction principale pour gérer les mots de passe
def main():
    passwords = load_passwords()

    while True:
        print("Que voulez-vous faire ?")
        print("1. Ajouter un nouveau mot de passe")
        print("2. Afficher les mots de passe existants")
        print("3. Quitter")

        choice = input("> ")

        if choice == "1":
            website = input("Site web : ")
            username = input("Nom d'utilisateur : ")
            password = input("Mot de passe : ")

            hashed_password = hash_password(password)

            passwords[website] = {
                "username": username,
                "password": hashed_password
            }

            save_passwords(passwords)

            print("Le mot de passe a été enregistré avec succès !")

        elif choice == "2":
            if len(passwords) == 0:
                print("Aucun mot de passe enregistré.")
            else:
                print("Voici la liste des mots de passe enregistrés :")
                for website, data in passwords.items():
                    print(f"{website} - Nom d'utilisateur : {data['username']}, Mot de passe : {data['password']}")
        elif choice == "3":
            break
        else:
            print("Choix invalide.")

    main()
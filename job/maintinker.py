# def chinker(shinker):
#     window = tk.Tk()
#     window.title("acueil")

#     username_label = tk.Label(window, text="Nom d'utilisateur:")
#     username_entry = tk.Entry(window)

#     password_label = tk.Label(window, text="Mot de passe:")
#     password_entry = tk.Entry(window, show="*")

#     submit_button = tk.Button(window, text="Soumettre")

#     username_label.grid(row=0, column=0)
#     username_entry.grid(row=0, column=1)

#     password_label.grid(row=1, column=0)
#     password_entry.grid(row=1, column=1)

#     submit_button.grid(row=2, column=1)
#     # Fonction pour hacher un mot de passe
import re
import hashlib
import json
import tinker as tk


    
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

def submit_credentials():
    
    window = tk.Tk()
    window.title("acueil")

    username_label = tk.Label(window, text="Nom d'utilisateur:")
    username_entry = tk.Entry(window)

    password_label = tk.Label(window, text="Mot de passe:")
    password_entry = tk.Entry(window, show="*")

    submit_button = tk.Button(window, text="Soumettre")

    username_label.grid(row=0, column=0)
    username_entry.grid(row=0, column=1)

    password_label.grid(row=1, column=0)
    password_entry.grid(row=1, column=1)

    submit_button.grid(row=2, column=1)
    username = username_entry.get()
    password = password_entry.get()
    
    if len(password) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
    elif not any(char.isdigit() for char in password):
        print("Le mot de passe doit contenir au moins un chiffre.")
    elif not any(char.isupper() for char in password):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
    elif not any(char.islower() for char in password):
        print("Le mot de passe doit contenir au moins une lettre minuscule.")
    elif:
        print("Nom d'utilisateur:", username)
        print("Mot de passe:", password)
    else:
        hashed_password = hash_password(password)
        passwords[password] = {
            "password": hashed_password
            }
        save_passwords(passwords)
        print("Le mot de passe a été enregistré avec succès !")
        

submit_credentials()
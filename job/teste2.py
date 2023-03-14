import re
import hashlib
import json
import tkinter as tk

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

def add_password():
    global username_entry, password_entry, status_label, passwords
    username = username_entry.get()
    password = password_entry.get()
    if len(password) < 8 or len(password) > 40:
        status_label.config(text="Le mot de passe doit contenir entre 8 et 40 caractères.")
    elif not re.search(r"[A-Z]", password):
        status_label.config(text="Le mot de passe doit contenir au moins une lettre majuscule.")
    elif not re.search(r"[a-z]", password):
        status_label.config(text="Le mot de passe doit contenir au moins une lettre minuscule.")
    elif not re.search(r"[0-9]", password):
        status_label.config(text="Le mot de passe doit contenir au moins un chiffre.")
    elif not re.search(r"[!@#$%^&*]", password):
        status_label.config(text="Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
    elif username in passwords:
        status_label.config(text="Ce nom d'utilisateur a déjà été enregistré.")
    else:
        hashed_password = hash_password(password)
        passwords[username] = {
            "password": hashed_password
        }
        save_passwords(passwords)
        status_label.config(text="Le mot de passe a été enregistré avec succès !")

def show_passwords():
    global status_label, passwords
    if len(passwords) == 0:
        status_label.config(text="Aucun mot de passe enregistré.")
    else:
        status_label.config(text="Voici la liste des mots de passe enregistrés :")
        for password, data in passwords.items():
            status_label.config(text=status_label.cget("text") + f"\n-> Nom d'utilisateur : {password}, Mot de passe crypté : {data['password']}")

def principale():
    global passwords, username_entry, password_entry, status_label
    passwords = load_passwords()
    
    # Créer une fenêtre Tkinter
    fenetre = tk.Tk()
    fenetre.title("Gestionnaire de mots de passe")
    
    # Ajouter des widgets pour entrer un nom d'utilisateur et un mot de passe
    username_label = tk.Label(fenetre, text="Nom d'utilisateur : ")
    username_label.grid(row=0, column=0, padx=5, pady=5)
    username_entry = tk.Entry(fenetre)
    username_entry.grid(row=0, column=1, padx=5, pady=5)
    
    password_label = tk.Label(fenetre, text="Mot de passe : ")
    password_label.grid(row=1, column=0, padx=5, pady=5)
    password_entry =
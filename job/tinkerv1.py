import re
import hashlib
import json
from tkinter import *

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

# def  verif_login(username, password):
#     with open('users.json') as f:
#         users = json.load(f)

#     for user in users:
#         if user['username'] == username and user['password'] == password:
#             window.geometry("1080x800")
#             label_title.destroy()
#             label_subtitle.destroy()
#             username_entry.destroy()
#             label_mot_de_passe.destroy()
#             password_entry.destroy()
#             confirme_password_button.destroy()
#             result_label.destroy()


def submit_credentials():
    username = username_entry.get()
    password = password_entry.get()
    # verif_login
        # Vérifier si l'utilisateur existe dans le fichier JSON et si le mot de passe correspond
    if username in passwords and passwords[username]["password"] == hash_password(password):
        window.geometry("1080x800")
        label_title.destroy()
        label_subtitle.destroy()
        username_entry.destroy()
        label_mot_de_passe.destroy()
        password_entry.destroy()
        confirme_password_button.destroy()
        result_label.destroy()
        
        new_subtile = Label(frame, text=new_user, font=("Courrier", 10), bg='orange')
        new_subtile.pack()

        

    else:
        result_label.config(text="Nom d'utilisateur ou mot de passe incorrect.")
    
    # Effacer les champs de l'interface graphique après la tentative de connexion



    if len(password) < 8 or len(password) > 40:
        result_label.config(text="Le mot de passe doit contenir entre 8 et 40 caractères.")
    elif not re.search(r"[A-Z]", password):
        result_label.config(text="Le mot de passe doit contenir au moins une lettre majuscule.")
    elif not re.search(r"[a-z]", password):
        result_label.config(text="Le mot de passe doit contenir au moins une lettre minuscule.")
    elif not re.search(r"[0-9]", password):
        result_label.config(text="Le mot de passe doit contenir au moins un chiffre.")
    elif not re.search(r"[!@#$%^&*]", password):
        result_label.config(text="Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
    else:
        hashed_password = hash_password(password)
        passwords[username] = {
            "password": hashed_password
        }
        save_passwords(passwords)
        result_label.config(text="Le mot de passe a été enregistré avec succès !")
        
        # Efface les champs de l'interface graphique après avoir enregistré le mot de passe

# Charge les mots de passe existants ou crée un nouveau fichier si aucun n'existe
passwords = load_passwords()

# Interface graphique avec tkinter
window = Tk()
window.title("acueil")
window.geometry("1080x720")
window.minsize(480, 360)
window.config(background='#41B77F')


#ajout d'un texte de bvn
label_title = Label(window, text="Bienvenue sur crée votre mot de passe", font=("Courrier", 20), bg='#41B77F')
label_title.pack()
# le titre de nom utilisateur
frame= Frame(window, bg='grey')
frame.pack(expand=True)

label_subtitle = Label(frame, text="Nom d'utilisateur:", font=("Courrier", 10), bg='orange')
label_subtitle.pack(padx=10, pady=10)

username_entry = Entry(frame)
username_entry.pack()

label_mot_de_passe = Label(frame, text="mot de passe:", font=("Courrier", 10), bg='orange')
label_mot_de_passe.pack(padx=10, pady=10)

password_entry = Entry(frame, show="*")
password_entry.pack()

confirme_password_button = Button(frame, text="Confirmer:", font=("Courrier", 10), bg='orange', command=submit_credentials)
confirme_password_button.pack()

result_label = Label(window, text="")

new_user = username_entry
window.mainloop()
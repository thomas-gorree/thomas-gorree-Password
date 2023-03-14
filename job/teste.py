
mot_de_passe = input("donner votre mot de passe\n")


def valide(password):
    if len(password) < 8 or len(password) > 40:
        print("le mot de passe doit étre entre 8 a 40 caratère") 
    
    minuscule = False
    majuscule = False
    chiffre = False
    spéciale = False
    
    for i in range(len(password)):
        if password[i] >= "a" and password[i] <= "z":
            minuscule = True
        if password[i] >= "A" and password[i] <= "Z":
            majuscule = True
        if password[i] >= "0" and password[i] <= "9":
            chiffre = True
        if password[i] == "#" or password[i] == "!" or password[i] == "@" or password[i] == "$" or password[i] == "%" or password[i] == "^" or password[i] == "&" or password[i] == "*":
            spéciale = True

    if minuscule == False :
        print("le mot de passe doit contenir une minuscule") 

    if majuscule == False :
        print("le mot de passe doit contenir une majuscule")

    if chiffre == False :
        print("le mot de passe doit contenir un chiffre")

    if spéciale == False :
        print("le mot de passe doit contenir un caractére spéciale")

    if minuscule== True and majuscule== True and chiffre== True and spéciale== True:
        print("les exigences de sécurité son  respecter")

valide(mot_de_passe)
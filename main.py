"""nom = "Mady"
print("Je m'appelle " + nom)
print("Mon nom c'est bien " + nom + " CISSE")

prenom = input("Quel est ton prenom? ")
print("Je m'appelle " + prenom)
print("Mon nom c'est bien " + prenom + " CISSE")"""

"""ton_nom = input ("Quel est vous nom? ")
ton_age = input("Quel est vous age? ")
print("vous vous appellez " + ton_nom + ", vous avez " + ton_age + "ans")"""

""" # Convertir un entier en une chaine de caractére
# ton_nom = input ("Quel est vous nom? ")
# ton_age = input("Quel est vous age? ")
age = 25
annee_prochaine = age + 1
print("vous avez " + str(age) + "ans.")
print("Année prochaine, vous aurez " + str(annee_prochaine) + "ans.")"""

"""
# Convertir une chaine de caractére en entier
# ton_nom = input ("Quel est vous nom? ")
age = input("Quel est vous age? ")
# age = 25
try:
    annee_prochaine = int(age) + 1
except:
    print("ERREUR: vous devez entrer un nomber")
else:
    print("vous avez " + str(age) + "ans.")
    print("Année prochaine, vous aurez " + str(annee_prochaine) + " ans.")
"""

# La boucle while: "tant que"
"""
n = 0
while(n < 10):
    print("La valeur de n:" + str(n))
    n = n + 1
"""

"""mot_de_pass = ""
while not mot_de_pass == "password":
    mot_de_pass = input("Entrer votre mot de passe: ")
print("Votre de passe est correte, vous avez accée à votre compte")"""

"""votre_nom = ""
while votre_nom == "":
    votre_nom = input("Quel est votre nom? ")
print("Votre nom est " + votre_nom)"""


def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quel est votre nom? ")
    return nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input("nom_personne " + "quel est votre age? ")
        age_int = int(age_str)
    return age_int


def affichage(nom, age):
    print()
    print("vous vous appellez " + nom + ", vous avez " + str(age) + " ans")
    print("Année prochaine, vous aurez " + str(age + 1) + " ans.")
    if age == 17:
        print("Vous etes mineur")
    elif 1 < age < 3:
        print("Vous etes un bebe")
    else:
        print("Vous ete majeur")


nom1 = demander_nom()
nom2 = demander_nom()

age1 = demander_age(nom1)
age2 = demander_age(nom2)

affichage(nom1, age1)
affichage(nom2, age2)




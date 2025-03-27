# Bonjour monsieur je suis KADJO ALLOUAN MOÏSE BIENVENUE
# GRP 12,13,14

# Exercice 1 : Calcul de l’aire d’un rectangle

print("  CALCUL DE L'AIRE D'UN RECTANGLE")
print()
i=0
while i<1:
    try:
        L=float(input(print("Entrez la longueur du rectangle :")))
    except ValueError :
        print("⚠️ attention la longueur doit être un nombre")
    else:
        if L<0:
            print("⚠️ un nombre positif SVP")
        else:
          i=i+1
while i<2:
    try:
        l=float(input(print("Entrez la largeur du rectangle :")))
    except ValueError :
        print("⚠️ attention la longueur doit être un nombre")
    else:
        if l<0:
            print("⚠️ un nombre positif SVP")
        else:
            i=i+1
print("l'aire du rectangle est de ",l*L,"unités carrées")      
print()
print()

#Exercice 2 : Conversion de température

print("CONVERTION DE TEMPÉRATURE")
print()

while i<3:
    try:
        dc=float(input(print("Entrez une température en degré celsius :")))
    except ValueError :
         print("⚠️ attention la température doit être un nombre")
    else:
        i=i+1
print(dc,"degré celsius équivaut à ",dc*9/5+32," degrés Fahrenheit.")
print()
print()

# Exercice 3 : Vérification de parité

print("  VERIFICATION DE PARITÉ")
print()
while i<4:
    try:
        n=int(input(print("Entrez un nombre entier :")))
    except ValueError :
        print("⚠️ attention il faut un nombre")
    else:
        i=i+1
if n%2==0:
    print("le nombre",n,"est pair")
else:
    print("le nombre",n,"est impair")
print()
print()


# Exercice 4 : Calcul de la somme des nombres pairs

print(" CALCUL DE LA SOMME DES NOMBRES PAIRS")
print()
while i<5:
    try:
        m=int(input(print("Entrez un nombre entier :")))
    except ValueError :
        print("⚠️ attention il faut un nombre")
    else:
        i=i+1
b=0
for i in range(1,m+1):
    if i%2==0:
        b=b+i
print("La somme des nombres pairs de 1 à",m,"est de",b)
print()
print()

#Exercice 5 : Recherche de caractères dans une chaîne

print(" RECHERCHE DE CARACTÈRE DANS UNE CHAÎNE")
print()
ch=str(input(print("Ecrivez votre text:")))
car=str(input(print("quelle lettre chercher vous à connaître le nombre ?:")))
t=0
for i in ch:
    if i==car:
        t=t+1
print("la lettre '"+car+"' apparaît",t,"fois dans votre texte")

# Bonne suite de journée à vous monsieur 😇😇😇
# JEU EN CODING

from random import*

print("ce jeu consiste à deviner le nombre tiré par l'ordinateur")
print()
a=randint(1,30)
i=5
while i>1:
    try:
        n=int(input("Entrer un nombre entre 1 et 30:"))
    except ValueError:
        print ("entrer un nombre entier ")   
    if n<1:
        print("le nombre doit être sup ou égale à 1")
    elif n>30:
        print("le nombre doit être inf ou égale à 30")
    elif n==a:
        print("votre proposition :",n,"bravo! vous avez gagné")
        i=i-5
    elif n>a:
        print("votre proposition :",n,"trop grand")
        i=i-1
    else:
        print("votre proposition :",n,"trop petit")
        i=i-1

print()
if n!=a:
    print("Désolé vous avez échoué sûrement  vous gagnerez une autre fois")
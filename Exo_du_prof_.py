# Programme effectué par 
# KADJO ALLOUAN MOISE BIENVENUE (KAMB)

import calendar  as ca

# Exo 1 
print('Exercice1')

print('CALCUL DE COMBINAISON "nCp"')
print()

def fact(x):
    if x<2:
        return 1
    else:
        return x*fact(x-1)

          
n=int(input("entrer la valeur de n:"))
p=int(input("entrer la valeur de p:"))

print('la combinaison de ',p,'dans',n,'est',end="")
print(' ',int(fact(n)/(fact(p)*fact(n-p))))

print()

# Ex2
print('Exercice 2')

# ce programme consiste à saisir le nom et le numero de 5 etudiant

for i in range(1,6):
    etud=input(print("veillez entré le nom de l'étudiant",i,':'))
    num=int(input(print("veillez entrer le numero de l'etudiant",i,':')))

#Ex3
print('Exercice 3')


print("ce programme consiste à dir si une année est bissextile ou pas")
print()
ans= int(input("Entrer l'année : ")) 

if ca.isleap(ans)==True:
	print("l'anné ",ans,"est bissextile")
else :
	print("l'anné ",ans," n'est pas bissextile")

    
# Bonjour monsieur je suis KADJO ALLOUAN MOÏSE BIENVENUE
# GRP 12,13,14

print("ce programme consiste à résoudre   une equa de 2nd degré de la forme ax²+bx+c")
print()

from math import*

def equa(a,b,c):
    delta=b*b-4*a*c
    if delta==0:
        print("l'equa admet une solution double")
        x=(-b)/2*a
        return x
    elif delta>0:
        print("l'equa admet deux solutions")
        x1=((-b)+sqrt(delta))/2*a
        x2=((-b)-sqrt(delta))/2*a
        print("x1=",x1,"et x2=",x2)
    else:
        print("votre equa n'a pas de solution")
  


 
b=float(input(print("saisir b:")))
c=float(input(print("saisir ç:")))
try:
    a=float(input(print("saisir a:")))
    while a==0:
        a=float(input(print("a doit être
    print(a)
except typeerror:
    print("veillez entre un nombre")
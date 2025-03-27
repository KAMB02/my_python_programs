# Bonjour monsieur je suis KADJO ALLOUAN MOÏSE BIENVENUE
# GRP 12,13,14

print("ce programme consiste à résoudre   une equa de 2nd degré de la forme ax²+bx+c")
print()

from math import*

def equa(a,b,c):
    delta=b*b-4*a*c
    if delta==0:
        print("votre equation admet une solution double")
        x=(-b)/2*a
        return print("x=",x)
    elif delta>0:
        print("votre equation admet deux solutions")
        x1=((-b)+sqrt(delta))/2*a
        x2=((-b)-sqrt(delta))/2*a
        print("x1=",x1,"et x2=",x2)
    else:
        print("votre equation n'a pas de solution")
        
        
i=0
while i<1:
    try:
        a=float(input("la valeur de a:"))
    except ValueError:
        print("⚠️ attention a doit être un nombre ")
    else :
        if a==0:
            print("⚠️ attention a doit être non nul")
        else:
            i=i+1 
print()

while i<2:
    try:
        b=float(input("la valeur de b:"))
    except ValueError:
        print("⚠️ attention b doit être un nombre ")
    else:
        i=i+1
print()

while i<3:
    try:
        c=float(input("la valeur de c:"))
    except ValueError:
        print("⚠️ attention c doit être un nombre ")
    else:
        i=i+1
print()

print(equa(a,b,c))

# bonne suite de journée à vous monsieur 😇😇
   


from encodings import utf_8


# KADJO ALLOUAN MOISE BIENVENUE
# Licence 2 SI

# Exercice 2

#1)

def ind(liste_entier,val):
    
    if(val not in liste_entier):
        print("l'element ",val,"n'est pas dans la liste")
    else:
        i=len(liste_entier)
        
        while(i>0):
            if(liste_entier[i-1]==val):
                print("l’indice du denier  ",val,"est",i-1)
                break
            else:
                i-=1
print("recherche du dernier index d'un nombre dans la liste\n")

list=[1,2,5,3,2,5,78,22,1,5,3]
print(list,"\n")
el=int(input("Quelle élément cherchez vous le index ?: "))
ind(list,el)

print("\n\n")

# 2_a)
print(" cette partie consiste à enregistrer des entiers dans une liste \n")

nb=int(input("entrer la taille de la liste :"))
print("\n")
liste_notes=[]
while(nb>0):
    note=float(input("entrer un nombrer comprise entre 0 et 20 : "))
    if(note<0 and note >20):
        print("la note dois etre comprise entre 0 et 20 \n")
        continue
    else:
        liste_notes.append(note)
        nb-=1
#print( liste_notes)
        
# 2_b)
# déterminer la merlleure , la mauvaise et la moyenne dans la liste donnée

print("la meilleure note est: ",max(liste_notes),"\nla mauvaise note est :",min(liste_notes),"\n")
print("la moyenne de toutes les notes est :",sum(liste_notes)/len(liste_notes),"\n\n")

# 3)
print("On cherche a calculé le Tribonacci d'un nombre donné\n")

def Tribonacci(n):
    u0,u1,u2=0,0,1
    if(n==0 or n==1):
        return 0
    elif(n==2):
        return 1
    elif(n>2):
        return Tribonacci(n-1)+Tribonacci(n-2)+Tribonacci(n-3)
        
n=int(input("entrer la valeur dont vous volez son Tribonacci:"))
print("Tribonacci(",n,")=",Tribonacci(n))

    
    
        



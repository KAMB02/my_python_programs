# Calcule du PGCD et du PPCM

print("ce programme consiste à calculer le PGCD et le PPCM de deux nombre\n")

#-------------------------------------------------

def PGCD ( nbr1 , nbr2 ):
    if ( nbr1 == 0 ):
        return nbr2 
    elif ( nbr2 == 0 ) :
        return nbr1 
    else:
        return PGCD( nbr2 , nbr1 % nbr2 )
    
 #------------------------------------------------- 
      
def PPCM( nbr1 , nbr2):
    if (PGCD(nbr1,nbr2) !=0):
        return int((nbr1*nbr2)/PGCD(nbr1,nbr2) )
    return 0

#-------------------------------------------------
def Give_number():

    while True:
        try:
            valeur=int(input("Veillez entrer un entier : " ))

        except ValueError:
            print(" Attention le nombre doit être un entier positive ")
            continue
        if ( valeur<0 ) : 
            print("Attention le nombre doit être un entier positive ")
        else:
            break
    return valeur

def result(opera:int ):
    a = Give_number() 
    b = Give_number()
    if opera== 1:
        print(f"PPCM({a},{b}) = {PPCM(a,b)}")
    else :
        print(f"PGCD({a},{b}) = {PGCD(a,b)}")
    
print("\n----------------\n1 --> calcul de PGCD(a,b) \n2 --> calcule de PPCM(a,b)\n3 --> quitter le programme\n----------------\n")
choix=int(input("choisissez entre 1 , 2 et 3 :"))
print("\n")
while True :

    match choix:
        case 1:
            result(2)
        case 2:
            result(1)
        case _:
            print("voulez vous quitter le programme ?")
    choix_quit=input("taper 3 pour quitter autres touche pour continuer :")
    if choix_quit=="3":
        break
    else:
        continue
        
        


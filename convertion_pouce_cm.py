
def demander_et_convert(unit1:str,unit2:str,coef:float):
    # cette fonction permet de demander et d'afficher la convertion d'un nombre 
    valeur=float(input(f"Conversion de {unit1}  -> {unit2},Entre la valeur a convertir en {unit1}:"))
    print(f" Resultat de la convertion : {round(valeur*coef,3)} ")

# choix de l'utilisateur{unit1} = {round(valeur*coef,3)} {unit2}")

print("\nCE PROGRAMME CONSISTE A CONVERTIR DE POUCE EN cm ET VISE VERSA\n-------------------------------------------------------\n")
print("** 1 : pouce -> cm \n** 2 : cm -> pouce \n** 3 :  quitter le programme \n-------------------------------------------------------\n")
choix=int(input("Faite votre choix ( 1 , 2 , 3 )  : "))


while True :
    match choix:
        case 1:
            demander_et_convert("pouce","cm",2.54)
        case 2:
            demander_et_convert("cm","pouce",0.394)
        case 3:
             break   
        case _ :
            print(" ⛔ Attention vous devez choisir 1 , 2 ou 3\n")

    choix_de_sortir=int(input("Taper 3 pour quitter et autre numero pour continuer :"))
    if (choix_de_sortir==3):
        break
    else :
        continue
    # si l'utilisateur entre c on continue sinon on sort du programme 
'''
match choix_de_sortir:
    case "c":
        continue
    case default:
        break
'''        
print("\n--------------------------------------------------------\nFIN DU PROGRAMME\n")  
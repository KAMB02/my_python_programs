
import calendar  

print("ce programme consiste à afficher le calendrier de l'année choisir")
print()
ans= int(input("Entrer l'année : ")) 

for moi in range (1,13):  
    print(calendar.month(ans, moi))  

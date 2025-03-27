ch=input("entrer un texte : ")
rec=input("entrer l'expression dont vous cherchez le nombre d'occurence ")
nb=0
for i in range (len(ch)-1):
    if(rec==ch[i:i+len(rec)]):
        nb+=1
print ("l'expression "+rec+"apparaît",nb,"fois dans le texte \n")       
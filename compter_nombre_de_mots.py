ch=str(input(print("insérer votre texte",)))
mot=str(input(print("entrer le mot chercher",)))
n=0
for i in ch:
    if i==mot:
        n=n+1
print("le texte contient ",n,mot)
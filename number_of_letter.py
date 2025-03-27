#mon exo
ch=str(input(print("insérer votre texte",)))
p=int(input(print("combien de lettre voulez vous connaitre le nombre? ",)))
for j in range(p):
    mot=str(input(print("entrer la lettre chercher",)))
    n=0
    for i in ch:
        if i==mot:
            n=n+1
    print("le texte contient ",n,mot)
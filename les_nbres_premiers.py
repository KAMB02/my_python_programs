# enumeration des n nombres premiers
print("  CE PROGRAMME CONSIST À ÉNUMÉRÉ") 
print("  LES NOMBRES PREMIERS ENTRE 1 ET n")
print ()
n=int(input("Entrer un nombre entier n :"))
print ()
print("les nombres premiers entre 1 et",n,"sont:")
          
for i in range (1,n+1):
    ndiv=0
    for j in range(1,i+2):
        if i%j==0:
            ndiv+=1  
    if ndiv==2:
        print(i)
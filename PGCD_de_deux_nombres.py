# Calcule du pgcd
print("ce programme consiste à calculer le pgcd de deux nombre")

a=0
while a<1:
    try:
        n=int(input(print(" valeur de n:")))
    except ValueError:
        print(" attention n doit être un entier")
    else :
        if (n<0):
            print("attention n doit être positif ")
        else:
            a=a+1
            
while a<2:
    try:
        m=int(input(print(" valeur de m:")))
    except ValueError:
        print(" attention m doit être un entier")
    else :
        if (m<0):
            print("attention m doit être positif ")
        else:
            a=a+1
            
if n>m:
    x=n
    y=m
else:
    x=m
    y=n
R=0
while x%y !=0:
    R=x%y
    x=y
    y=R
print("PGCD("+str(n)+","+str(m)+")=",y)
    
    
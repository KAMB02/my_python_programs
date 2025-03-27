# cet programme consite à tester si
# un nombre est fort
print("TEST DE NOMBRE FORT")
print()
def facto(k):
    if k<=1:
        return 1
    else :
        return k*facto(k-1)

n=int(input("entrer la valeur de n:"))
m=n
s=0
while n!=0:
    c=n % 10
    s=s+facto(c)
    n=n//10
 
if s==m :
    print(m," est un nombre fort")
else:    
    print(m," n'est pas un nombre fort")    
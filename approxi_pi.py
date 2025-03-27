# approximation de π
print("CE PROGRAMME CONSISTE A FAIRE UNE APPROXIMATION DE pi\n\n")

def puiss(n):
    if n%2==0:
        return 1
    else:
        return -1
        

while True:
    try:
        n=int(input("valeur de l'approximation :"))
    except ValueError:
        print(" attention la valeur doit être un entier ")
    else:
        break
        
b,pi=0,0
for i in range(n):
    b=2*i+1
    pi=pi+puiss(i)/b
print(4*pi)
  
# trouver le premier nombre entier verifiant 2^n>=k
print(" le 1er entier verifiant 2^n>k")
print()
def puiss2(k):
    n=0
    while 2**n<k:
        n+=1
    return n

a=int(input("valeur de a:"))
print(puiss2(a))
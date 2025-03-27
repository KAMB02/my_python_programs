 # trie par sélection


def trie_select(L):
    for i in range(len(L)-1):  
        M,T=i,[]
        for j in range(i+1,len(L),1):
            if L[j] <L[M]:         
                T=L[M]
                L[M]=L[j]
                L[j]=T
    return L
nb=int(input("entre la taille de votre liste:"))
i=0
List=[]
while i<nb:
    ids=int(input(print("entrer la valeur du",i+1,':')))
    List+=[ids]
    i+=1

    
    

print( trie_select(List))                
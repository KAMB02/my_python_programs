# ce programme à été effectuer par
# Kadjo Allouan Moïse Bienvenue (KAMB)

print("ce programme consiste à affiché \nla sommme des inverse des n premiers entier non nul \n\n") 

n=int(input("Entrer un entier pour la valeur de n:"))

som=1
ch="1+"
for i in range (2,n+1):
    ch+=str(1)+"/"+str(i)+"+"
    som+=1/i
sh=ch[0:len(ch)-1]  
print(sh,"=",som)   
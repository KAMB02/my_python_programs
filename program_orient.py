class Personne:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=age
        
           
    def sepresenter(self):
        print("bonjour je m'appelle ",self.nom,"j'ai" , self.age,"ans")
        if self.estmajeur():
            print(" je suis majeur")
        else:
            print(" je suis mineur")
    
    def estmajeur(self):
        return self.age>=18         
      
personne1=Personne("jean",10)

personne1.sepresenter()
        
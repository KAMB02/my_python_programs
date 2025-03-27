def recuperer_et_afficher_info_personne(num):
    nom = input("nom de la personne "+str(num)+" :")
    age = input("age de la personne "+str(num)+" :")
    print("la personne ",str(num),"est",nom,"son age est:",age,"ans")
    print("le nom ",str(num),"comporte",len(nom),"caractères")
''#
recuperer_et_afficher_info_personne(1)
recuperer_et_afficher_info_personne(2)


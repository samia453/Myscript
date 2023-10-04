# ecrire un programme qui va lire les donnees d un employer a partir d un clavier
# identifiant, nom, salaire, adresse, marie

id = int(input("saisir votre ID svp: "))
nom = input("saisir votre nom svp : ")
salaire = float(input("Veuillez saisir votre salaire : "))
adresse = input("Veuillez saisir votre adresse : ")
Status = bool(input("etes vous marié [true | false] :"))
print("le id de l employe est: ", id )
print("le nom de l employe est: ", nom )
print("le salaire de l employe est: ", salaire )
print("le l adresse de l employe est: ", adresse)
print("lest ce que vous etes marie: ", Status)
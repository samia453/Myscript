# ecrire un programme qui choisi le plus grand nombre parmi deux nombre
n1 = int(input("saisir un nombre 1 svp : "))
n2 = int(input("saisir un nombre 2 svp : "))

if n1 > n2:
   print ("le nombre 1 est superiere au nombre 2")
elif n1 == n2 :
    print("Le nombre 1 et 2 sont identique")
else:
   print("le nombre 2 est superieur a nombre 1")
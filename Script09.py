#ecrire un programme qui choisi le plus grand nombre parmi 3 nombres a partir du clavier

n1 = int(input("Veuillez saisir le nombre 1 : "))
n2 = int(input("Veuillez saisir le nombre 2 : "))
n3 = int(input ("Veuillez saisir le nombre 3 : "))

if n1 > n2 and n1 > n3:
    print ("le nombre 1 est superieur au nombre 2 et au nombre 3 ")
elif  n2 > n3:
    print ("le nombre 2 est superieur au nombre 1 et au nombre 3")
else:
    print("le nombre 3 est superieur au nombre 1 et au nombre 2")
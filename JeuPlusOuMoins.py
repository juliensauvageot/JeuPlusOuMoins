from random import randrange
 
nombrePropose = 0

nombreMystere = randrange(1, 100)

print(nombreMystere)
 
while nombrePropose != nombreMystere:
     
    print("Quel est le nombre ?")
 
    nombrePropose = input()
 
 
    if nombrePropose < nombreMystere:
        print("C est trop petit !")
 
    if nombrePropose > nombreMystere:
        print("C est trop grand !")
 
    else:
        print("Felicitations, vous avez trouve le nombre mystere !!!")
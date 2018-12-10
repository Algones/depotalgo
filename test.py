"""
liste = ["Tele", "Frigo", "Voiture", "scooter", "Trotinette","Casque"]


for x in liste:
    print x

x = 0
while x < len(liste):
    print liste[x]
    x += 1
"""

"""
def SayHello(name):
    if name:
        print ("Hello " + name)
    else:
        name = raw_input("Vous n'avez pas saisi de nom, merci d'en saisir un !! :) \n ")
        SayHello(name)

SayHello("")
"""

#Fibonnaci
def Fibonnaci(n):
    c = 0
    a = 0
    b = 1
    while c < n :
        c = a + b
        print str(a) + " " + str(b) + " " + str(c) 
        a = b
        b = c

Fibonnaci(int(raw_input("Entrez la limite pour la suite de Fibonnaci")))

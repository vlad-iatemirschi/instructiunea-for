'''Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele impare, pentru intervalul de la a la b (a și b se citesc de la tastatură).'''
a=int(input("Introdu a:"))
b=int(input("Introdu b:"))
if ((a%2)!=0):
    for n in range(a,b+1,2):
        print (n,end=" ")

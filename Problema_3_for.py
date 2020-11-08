"""Utilizînd ciclul FOR elaboraţi un program care afişează numerele pare, pentru intervalul de la 1 la n (n-este citit de la tastatură)."""
n=int(input("numarul este ="))
for p in range(1,n):
    if (p%2==0):
        print ("numarul par este",p)
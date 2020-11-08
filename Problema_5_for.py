"""Utilizînd ciclul FOR elaboraţi un program care calculeaza suma numerelor de la 1 la n, 
care se împart la 3 şi 5 pentru oricare n întrodus de la tastatură."""
n=int(input("numarul este"))
s=0
for i in range(1,n+1):
    if i%3==0 or i%5==0:
        s=s+i
print("suma =",s)
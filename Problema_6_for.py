"""Să se calculeze sumele: 	s1=1+2+3+…+n
			s2=1*2+2*3+3*4+…+(n-1)*n
			s3=1+1*2+1*2*3+…+1*2*3*…*n
			s4=12+22+32+…+n2
			s5=1/2+2/3+3/4+…+n/(n+1)
			s6=1+2+22+23+24+…+2n"""
n=int(input("primul numar este"))
s1=0
for p in range(1,n+1):
    s1+=p
print("prima suma este=",s1)

n=int(input("al doilea numar este"))
s2=0
for p in range(1,n+1):
    s2+=(p-1)*p
print("a doua suma este",s2)

n=int(input("al treilea numar este"))
s3=1
h=1
for p in range(2,n+1):
	h*=p
	s3+=h
print("a treia suma este",s3)

n=int(input("al patrulea numar este"))
s4=0
for p in range(1,n+1):
	s4+=(10*p+2)
print("a patra suma este",s4)

n=int(input("al cincilea numar este"))
s5=0
for p in range(1,n+1):
	s5+=n/(n+1)
print("a cincea suma este",s5)

n=int(input("al saselea numar este"))
s6=3
for p in range(2,n+1):
	m=str(p)
	s6+=int(str('2'+m))
print("a sasea suma este",s6)

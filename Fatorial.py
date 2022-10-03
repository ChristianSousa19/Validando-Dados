import math
n=int(input("Digite um numero: "))
f=n
l=1
print(" Calculando o fatorial de {}".format(n))
while n>0:
    print("{}".format(n),end=" ")
    print("x" if n > 1  else  "=" ,end=" ")
    l*=f
    n-=1
print("{} ".format(l))
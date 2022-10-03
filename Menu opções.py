n1=int(input("Digite o primeiro valor"))
n2=int(input("Digite o segundo valor"))
escolha=0
while escolha !=5:


   print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] novos números
[5] sair do programa''')
   escolha=int(input("Digite sua escolha: "))

   if escolha==1:
      soma = n1 + n2
      print(" A soma de {} mais {} é igual a {}".format(n1,n2,soma))
   elif escolha==2:
        multiplicar =n1*n2
        print( "A multiplicação de {} vezes {} é igual a {} :".format(n1,n2,multiplicar))
   elif escolha==3:
     if n1>n2 :
         maior=n1
     else:
         maior=n2
     print(" O maior valor digitado foi {}".format(maior))
   elif escolha==4:
    print("Informe os numeros novamnete:")
    n1=int(input("Digite o primeiro valor: "))
    n2=int(input("Digite o segundo valor: "))
   elif escolha !=5:
       print("Erro")
print("Fim do programa")
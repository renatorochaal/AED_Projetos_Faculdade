#Faça um Programa que leia três números e mostre o maior deles.

num_1 = int(input("Digite o primeiro numero: "))
num_2 = int(input("Digite o segundo numero : "))
num_3 = int(input("Digite o terceiro numero: "))

if(num_1 > num_2 and num_1 > num_3):
    maior = num_1
elif ( num_2 > num_3):
    maior = num_2
else:
    maior = num_3

print("O maior numero é: ", maior)

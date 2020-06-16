'''
#1 Faça um algoritmo que imprima os numeros no intervalo entre 1 e 100
i = 1
while (i < 100 and i >= 0):
    print(i)
    i += 1
'''
'''
#2 evolua o algoritmo no qual imprimimos os numeros num intervalo pré-definido para um algoritmo que pergunte ao usuário qual o intervalo que o mesmo deseja que seja impresso
num = int(input("Digite o intervalo que desejar: "))
for i in range(0, 100, num):
    print(i)
'''
'''
#3) Faça um algoritmo que imprima os números no intervalo entre 1 e 10 em ordem inversa:

for i in range(10, 1, -1):
    print(i)
'''
'''
#4) Faça um algoritmo que imprima os números pares entre 0 e 100:

for i in range(0, 100, 2):
    print(i)
'''
'''
#5) Faça um algoritmo que some a quantidade de números pares encontrados no intervalo entre 0 e 100:
total = 0
for i in range(0, 100, 2):
    if (i%2==0):
        total = total+1
print(total)
'''
#6) Faça um algoritmo que imprima os números primos entre 0 e 100:
limit = 20
for numero in range(2, limit):
    if limit % numero == 0:
        print("Não é primo :" + str(numero))
    else:
        print('É primo:', str(numero))


'''
#7) Faça um algoritmo que calcule os número primos num intervalo pré-determinado pelo usuário:
'''
'''
#8) Faça um algoritmo que imprima os valores no intervalo definido pelo usuário e permita que o mesmo possa definir 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela:
num1 = int(input("Digite o numero que se deve começar: "))
num2 = int(input("Digite o numero que deve terminar: "))
escolha = input("Digite 3 numero para serem ignorados na exibição, ex: 1,2,3: ")


for i in range(num1, num2):
'''
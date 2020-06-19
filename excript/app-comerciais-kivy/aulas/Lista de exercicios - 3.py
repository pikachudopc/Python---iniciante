#1) Faça um algoritmo que imprima os números no intervalo entre 1 e 100:
'''
comeco = 0
while comeco <= 100:
    print(comeco)
    comeco+=1

'''
#2) Evolua o algoritmo no qual imprimimos os números num intervalo pré-definido para um algoritmo que pergunte ao usuário qual o intervalo que o mesmo deseja que seja impresso:
'''
num = int(input("Digite o intervalo desejado: "))
for inter in range(0, 101, num):
    print(inter)
'''
#3) Faça um algoritmo que imprima os números no intervalo entre 1 e 10 em ordem inversa:
'''
for inverti in range(0,-11,-1):
    print(inverti)
'''
#4) Faça um algoritmo que imprima os números pares entre 0 e 100:
'''
for par in range(0,101,2):
    print(par)
'''
#5) Faça um algoritmo que some a quantidade de números pares encontrados no intervalo entre 0 e 100:
'''
soma=0
for par in range(0,100,2):
    soma+=1
print(soma)
'''
#6) Faça um algoritmo que imprima os números primos entre 0 e 100:
'''
for num1 in range(2,100):
    primo = True
    for num2 in range(2,num1):
        if (num1%num2==0):
            primo=False
    if primo:
        print(num1)
'''
#7) Faça um algoritmo que calcule os número primos num intervalo pré-determinado pelo usuário:
'''
inter = int(input("Digite o intervalo que quiser: "))
for num1 in range(2,101, inter):
    primo = True
    for num2 in range(2,num1, inter):
        if num1%num2 == 0:
            primo = False
    if primo:
        print(num1)
'''
#8) Faça um algoritmo que imprima os valores no intervalo definido pelo usuário e permita que o mesmo possa definir 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela:
'''
inter = int(input("Digite o intervalo que quiser: "))
print("#"*50)
print("Escolha 3 numero que não quer que apareção!")
not1=int(input("Primeiro numero: "))
not2=int(input("Segundo numero: "))
not3=int(input("Terceiro numero:"))
print("-"*50)
for num1 in range(2,101,inter):
    primo = True
    for num2 in range(2, num1,inter):
        if num1 % num2 == 0:
            primo = False
    if primo:
        if num1 not in {not1, not2, not3}:
            print(num1)
'''
#9) Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra. Caso a letra seja o "q" finalize a aplicação. Do contrário, imprima novamente a mesma frase até que o caractere "q" seja enviado:
'''
parar = "continuar"
primeira = 0
while parar != 'q':
    if primeira == 0:
        print("Estou em um loop, aperte 'q' para sair")
    parar = str(input("Digite: "))
    if parar != 'q':
        print("Se quiser sair precione 'q'")
    primeira = 1
'''
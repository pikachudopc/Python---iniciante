""""
#1) Faça um algoritmo que leia um numero e mostre se o mesmo é possitivo, negativo ou zero

numero = float(input("Digite um numero: "))

if(numero == 0):
    print("Seu numero é 0")
elif(numero > 0):
    print("Seu numero é Positivo: %.0f" %numero)
else:
    print("Seu numero é Negativo: %.0f" %numero)

"""
"""
#Faça um algoritmo que leia um numero e mostre se o mesmo é par ou impar!

numero = int(input("Digite um numero: "))

if(numero%2== 0):
    print("Seu numero é Par: %d" %numero)
else:
    print("Seu numero é Impar: %d" %numero)
"""
"""""
#Faça um algoritmo que leia dois numeros e imprima o maior

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um outro numero: "))

if(numero1>numero2):
     print("O maior numero é: %d" %numero1)
else:
     print("O maior numero é: %d" %numero2)



#Faça um algoritmo que peça a idade de uma pessoa e imprima na tela se a mesma já é maior de idade ou estão, se a mesma é de menor.

idade = int(input("Digite sua idade: "))

if (idade >= 18):
    print("Você é maior de idade!")
else:
    if((idade < 18) and (idade > 0)):
        print("Você é menor de idade!")
    else:
        print("Idade incorreta!")


#Faça um algoritmo que peça a idade do usuario e a idade da sua mãe. Em seguida, imprima na tela com quantos anos sua mãe o teve

myidade = int(input("Qual a sua idade: "))
mymom = int(input("Qual a idade da sua mãe:"))

birth = myidade - mymom

print("Sua mãe te concebeu com ", abs(birth))



#Faça um algoritmo que imprima 50 vezes o caractere "-" na tela (sem a utilização de laços de repetição

sinbolo = "-"

print(sinbolo*50)



#Faça um algoritmo que peça um numero ao usuario e verifique se o mesmo é par ou então impar
numero = int(input("Digite um numero: "))

if(numero%2== 0):
    print("Seu numero é Par: %d" %numero)
else:
    print("Seu numero é Impar: %d" %numero)
    

"""
"""
#Faça um algoritmo que peça dois numero. Primeiro, imprima o maior e, em seguida, o menor.
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if (num1 > num2):
    print("O maior numero é %d e o menor é %d" %(num1, num2))
elif (num1 == num2):
    print("Os dois numeros são iguais!")
else:
    print("O maior numero é %d e o menor é %d" %(num2, num1))


#Faça um algoritmo que verifica se um determinado valor é um numero inteiro

num1 = input("Digite um numero: ")

if (type(num1) == int):
    print("O numero digitado é inteiro!")
else:
    print("O numero digitado não é um inteiro!")
"""
"""
#Faça um algoritmo que verifica se um determinado valor é do tipo decimal

num1 = input("Digite um numero: ")


if (num1.isdecimal() == True):
    print("O valor digitado é decimal!")
else:
    print("O valor digitado não é decimal!")

"""
"""
#Faça um algoritmo que verifica se um determinado valor é do tipo String

num1 = input("Digite um numero: ")


if (num1.isalpha() == True):
    print("O valor digitado é String!")
else:
    print("O valor digitado não é String!")
"""
"""
#Faça um algoritmo que peça um valor numerico. Em seguida, Verifique se o numero é inteiro ou decimal.
num = input("Digite um numero: ").isnumeric()
print(type(num))
if(True):
    if(num)

"""

"""
#Faça um algoritmo que leia três numeros e imprima na tela o maior deles

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if((num1 > num2) and num1 > num3):
    print("O numero %d é o maior numero!" %num1)
if((num2 > num1) and num2 > num3):
    print("O numero %d é o maior numero!" %num2)
if((num3 > num2) and num3 > num1):
    print("O numero %d é o maior numero!" %num3)
"""
"""
#Faça um algoritmo que leia três numeros e imprima-os em ordem crescente

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if((num1 > num2) and (num1 > num3)):
    if((num2 > num3)):
        print("Os numeros digitados em ordem crescente são %d, %d e %d" %(num3,num2,num1))
    else:
        print("Os numeros digitados em ordem crescente são %d, %d e %d" % (num2, num3, num1))

if((num2 > num1) and (num2 > num3)):
    if((num1 > num3)):
        print("Os numeros digitados em ordem crescente são %d, %d e %d" %(num3,num1,num2))
    else:
        print("Os numeros digitados em ordem crescente são %d, %d e %d" % (num1, num3, num2))

if((num3 > num2) and (num3 > num1)):
    if((num2 > num1)):
        print("Os numeros digitados em ordem crescente são %d, %d e %d" %(num1,num2,num3))
    else:
        print("Os numeros digitados em ordem crescente são %d, %d e %d" % (num2, num1, num3))

"""
'''
#Faça um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não

testando = str(input("digite um caracter: "))

if (testando in {"a","e","i","o","u"}):
    print("É uma vogal!")
else:
    print("Não é uma vogal")
'''
"""
#Os endereços IP versão 4 são divididos em cinco classes: A, B, C, D e E.
# Os endereços no intervalo de 0 à 127 são classe A, de 128 a 191 são classe B, de 192 a 223 são classe C, de 224 à 239 são classe D e a partir de 240 são classe E.
# Faça um algoritmo que leia o primeiro octeto, no formato decimal de um endereço IP, e informe a sua classe.

ip = str(input("Informe o IP: "))
primeiro_octeto = int(ip.split(".")[0])

if (primeiro_octeto <= 127 and primeiro_octeto >= 0):
    print("A classe do ip é A!")
elif (primeiro_octeto >= 128 and primeiro_octeto <= 191):
    print("A classe do ip é B")
elif (primeiro_octeto >= 192 and primeiro_octeto <= 223):
    print("A classe do ip é C")
elif (primeiro_octeto >= 224 and primeiro_octeto <= 239):
    print("A classe do ip é D")
elif (primeiro_octeto >= 240 and primeiro_octeto <= 254):
    print("A classe do ip é E")

"""

"""
#Faça um algoritmo que receba um número inteiro, que represente um determinado mês do ano, e mostre o nome do mês correspondente. Por exemplo, se for informado o número 2, o algoritmo deverá exibir: fevereiro. O algoritmo também deve validar se a entrada está correta.

mes = int(input("Digite o numero do mês desejado(1-12): "))

if(mes >= 1 and mes <= 12):
    if(mes == 1):
        print("O mes digitado é Janeiro")
    elif(mes == 2):
        print("O mes digitado é Fevereiro")
    elif (mes == 3):
        print("O mes digitado é Março")
    elif (mes == 4):
        print("O mes digitado é Abriu")
    elif (mes == 5):
        print("O mes digitado é Maio")
    elif (mes == 6):
        print("O mes digitado é Junho")
    elif (mes == 7):
        print("O mes digitado é Julho")
    elif (mes == 8):
        print("O mes digitado é Agosto")
    elif (mes == 9):
        print("O mes digitado é Setembro")
    elif (mes == 10):
        print("O mes digitado é Outubro")
    elif (mes == 11):
        print("O mes digitado é Novembro")
    elif (mes == 12):
        print("O mes digitado é Dezenbro")
else:
    print("Digito incorreto, por favor tentar novamente!")
"""
'''
#Faça um algoritmo que valide uma data. A mesma deve ser formada por dia, mês e ano.
# Por exemplo, se o usuário digitar a data 10/8 a mesma será inválida. Porém, caso a data seja 01/10/2018, a mesma deve ser considerada válida.

data = str(input("Por favor, digitar uma data: "))

dia = int(data.split('/')[0])
mes = int(data.split('/')[1])
ano = int(data.split('/')[2])

if ((mes in {1,3,5,7,9,11}) and (dia >= 1 and dia <= 31)):
    if (ano >= 1000 and ano <= 2020):
        print("O ano digitado está correto: %d/%d/%d" %(dia,mes,ano))
elif ((mes in {2,4,6,8,10,12}) and (dia >=1 and dia <= 30)):
    if (ano >= 1000 and ano <= 2020):
        print("O ano digitado está correto: %d/%d/%d" % (dia, mes, ano))
else:
    print("algo deu errado, por favor tente novamente!")
'''


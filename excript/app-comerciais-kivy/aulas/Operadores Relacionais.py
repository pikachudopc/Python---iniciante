idade = int(input("Informe a sua idade: "))
if(idade<=0):
    print("A sua idade não poder ser 0 ou menor do que 0")
elif(idade>150):
    print("A sua idade não pode ser superior a 150 ano!")
elif(idade<18):
    print("Você precisa ter mais de 18 anos!")
else:
    print("Você pode entrar!")
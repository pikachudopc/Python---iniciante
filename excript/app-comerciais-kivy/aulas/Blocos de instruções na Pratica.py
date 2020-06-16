num1 = int(input("Digite um numero: "))


if(num1 > 10):
    print("O valor é maior do que 10!")
    if(num1<=15):
        print("o vamor é maior do que 10, mas menor que 15.")
    else:
        if(num1<=50):
            print("O valor é maior do que 10, mas menor do que 50!")
        else:
            print("o valor é maior do que 50")
else:
    if(num1>5):
        print("o numero é menor do que 10, mas é maior do que 5!")
        if(num1==7):
            print("o numero é igual a 7")
    else:
        print("O valor é menor do que 5.")
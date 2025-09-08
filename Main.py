## Atividade aula

UserChoice = int(input("Digite a operação que você quer (1 - soma, 2 - multiplicação, 3 - subtração): "))
Number1 = int(input("Digite o primeiro número que você quer manipular: "))
Number2 = int(input("Digite o segundo numero que você quer manipular: "))
## print(UserChoice)


def somar (a,b):
    return a + b

if (UserChoice == 1):
    print (f"soma = {somar(Number1, Number2)}")

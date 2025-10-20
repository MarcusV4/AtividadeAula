## Atividade aula

UserChoice = (input("Digite a operação que você quer (1 - soma, 2 - multiplicação, 3 - subtração, 4 - divisão): "))
Number1 = int(input("Digite o primeiro número que você quer manipular: "))
Number2 = int(input("Digite o segundo numero que você quer manipular: "))
## print(UserChoice)

## Atividade aula

#if UserChoice == 1:
    #resposta = Number1 + Number2
#elif UserChoice == 2:
 #   resposta = Number1 * Number2
#elif UserChoice == 3:
 #   resposta = Number1 - Number2

#print(resposta)    



def somar (a,b):
    return a + b

def dividir (a,b):
    return a / b

def multiplicar (a,b):
    return a * b

def quadratico (a, b):
    return a * a # erro proposital

if (UserChoice == 1):
    print (f"soma = {somar(Number1, Number2)}")
if (UserChoice == 4):
    print(f"divisão = {dividir(Number1, Number2)}")
if (UserChoice == 2):
    print(f"multiplicação {multiplicar(Number1, Number2)}")
if (UserChoice == 3):
    print(f"quadratico {quadratico(Number1, Number2)}")

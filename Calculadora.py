print("=== CALCULADORA ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opc = int(input("Digite uma opcao: "))

num1 = float(input("Escreva um numero: "))
num2 = float(input("Escrreva um numero: "))

match opc:
    case 1:
        print("Resultado", num1 + num2 )
    case 2:
        print("Resultado", num1 - num2 )    
    case 3:
        print("Resultado", num1 * num2 )
    case 4:
        if num2 == 0:
            print("Erro")  
        else:
            print("Resultado", num1 / num2)      
    case _:
        print("Opcao Invalida")        
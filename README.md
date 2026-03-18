# 🧮 Calculadora Simples em Python

Este é um projeto básico de uma calculadora feita em Python que permite realizar operações matemáticas simples diretamente pelo terminal.

## 📌 Funcionalidades

A calculadora oferece as seguintes operações:

* ➕ Soma
* ➖ Subtração
* ✖️ Multiplicação
* ➗ Divisão (com verificação de divisão por zero)

## 🛠️ Como funciona

1. O programa exibe um menu com as opções disponíveis.
2. O usuário escolhe uma operação digitando o número correspondente.
3. Em seguida, o usuário informa dois números.
4. O programa executa a operação escolhida e exibe o resultado.

## 💻 Código

```python
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
```

## ⚠️ Observações

* A divisão por zero é tratada para evitar erro no programa.
* Caso o usuário digite uma opção inválida, o sistema retorna uma mensagem de erro.
* O código utiliza a estrutura `match-case` (disponível a partir do Python 3.10).

## 🚀 Possíveis melhorias

* Adicionar loop para repetir operações sem reiniciar o programa
* Tratar erros de entrada (ex: letras em vez de números)
* Criar interface gráfica (GUI)
* Permitir mais operações (potência, raiz, etc.)

---
import os
import time
import platform

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

if platform.system() == 'windows':
    import msvcrt
else:
    import readchar

def getch():
    if platform.system() == 'windows':
        return msvcrt.getch().decode()
    else:
        return readchar.readchar()

def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primero número: "))
            operador = getch()
            num2 = float(input("Digite o segundo número: "))

            if operador == '+':
                resultado = num1 + num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
            elif operador == '/':
                resultado = num1 / num2
            else:
                print("Opção invalida. Digite um número.")
                continue
            limpar()   

            input(f"Resultado: {resultado}")

            print("Digite 'q' para sair ou 'enter' para continuar.")
            continuar = getch()
            if continuar.lower() == "q":
                break

            limpar()

        except ValueError:
            print("Digite um numero valido.")
            time.sleep(3)
            limpar()
        except ZeroDivisionError:
            print("Erro. Divisão por zero não é permitido")
            time.sleep(3)
            limpar()

if __name__ == "__main__":
        calculadora()
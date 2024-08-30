from calculadora import Calculadora

valorA = float(input("digite o primeiro valor: "))
valorB = float(input("digite o segundo valor: "))
operacao = input("digite a operação: ")

calculadora = Calculadora(valorA, valorB, operacao)

print(calculadora.calcular())
import sys

class Calculadora:
    def __init__(self, valorA, valorB, operacao):
        self.__valorA = valorA
        self.__valorB = valorB
        self.__operacao = operacao

@property
def valorA(self):
    return self.__valorA
@valorA.setter
def valorA(self, valorA):
    self.__valorA = valorA

@property
def valorB(self):
    return self.__valorB
@valorB.setter
def valorB(self, valorB):
    self.__valorB = valorB

@property   
def operacao(self):
    return self.__operacao
@operacao.setter    
def operacao(self, operacao):
    self.__operacao = operacao

def validarOperacao(simbolo):
    validos = ['+', '-', '*', '/']
    if simbolo in validos:
        return True
    else:
        return False
    
def calcular(self):
    if not self.validarOperacao():
        print("Operação inválida")
        sys.exit()
        return
    if self.__operacao == '+':
        print(self.__valorA + self.__valorB)
    elif self.__operacao == '-':
        print(self.__valorA - self.__valorB)
    elif self.__operacao == '*':
        print(self.__valorA * self.__valorB)
    elif self.__operacao == '/':
        if self.__valorB == 0:
            print("Erro: Divisão por zero")
            sys.exit()
            return
        print(self.__valorA / self.__valorB)
        return
    
def mostrarResultado(self):
      print(str(self.valorA) + ' ' + self.operacao + ' ' + str(self.valorB) + ' = ' + str(self.calcular()))
    

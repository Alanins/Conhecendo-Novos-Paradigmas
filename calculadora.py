class Calculadora:
    def __init__(self):
        self.__valorA = 0
        self.__valorB = 0
        self.__operacao = ""

    @property
    def valorA(self):
        return self.__valorA

    @valorA.setter
    def valorA(self, valor):
        self.__valorA = valor

    @property
    def valorB(self):
        return self.__valorB

    @valorB.setter
    def valorB(self, valor):
        self.__valorB = valor

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao

    def validarOperacao(self, simbolo):
        operacoes_validas = ['+', '-', '*', '/']
        return simbolo in operacoes_validas

    def calcular(self):
        if not self.validarOperacao(self.__operacao):
            print("Operação inválida. O programa será encerrado.")
            exit()

        if self.__operacao == '+':
            return self.__valorA + self.__valorB
        elif self.__operacao == '-':
            return self.__valorA - self.__valorB
        elif self.__operacao == '*':
            return self.__valorA * self.__valorB
        elif self.__operacao == '/':
            if self.__valorB == 0:
                print("Erro: Divisão por zero. O programa será encerrado.")
                exit()
            return self.__valorA / self.__valorB

    def mostrarResultado(self):
        resultado = f"{self.__valorA} {self.__operacao} {self.__valorB} = {self.calcular()}"
        print(resultado)

    def entradaDados(self):
        self.valorA = float(input("Digite o valor A: "))
        self.valorB = float(input("Digite o valor B: "))
        self.operacao = input("Digite a operação (+, -, *, /): ")


calculadora = Calculadora()

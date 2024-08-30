from Pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, dataNascimento, cpf, rg):
        self.__dataNascimento = dataNascimento
        self.__cpf = cpf
        self.__rg = rg


    @property
    def dataNascimento(self):
        return self.__dataNascimento
    @dataNascimento.setter
    def dataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        if len(cpf)!=14:
            raise ValueError("CPF deve ter 14 caracteres(no formato XXX.XXX.XXX-XX)")
        self.__cpf = cpf

    @property
    def rg(self):
        return self.__rg
    @rg.setter
    def rg(self, rg):
        self.__rg = rg  
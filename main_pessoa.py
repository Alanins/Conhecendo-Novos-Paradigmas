from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pessoa = Pessoa ("João", "12345678-9","2000-01-01", False)
pessoa_fisica = PessoaFisica("25-02-1991", "000.111.222-33", "15975388-1 ")
pessoa_juridica = PessoaJuridica("01-01-2019", "12.333.444/0001-22")


print("Instância da classe Pessoa:")
print(f"Nome: {pessoa.nome}")
print(f"Número da conta: {pessoa.numeroConta}")
print(f"Data de abertura da conta: {pessoa.dataAberturaConta}")
print(f"Status: {pessoa.status}")

print("Instância da classe PessoaFisica:")
print(f"Data de nascimento: {pessoa_fisica.dataNascimento}")
print(f"CPF: {pessoa_fisica.cpf}")
print(f"RG: {pessoa_fisica.rg}")

print("Instância da classe PessoaJuridica:")
print(f"Data de abertura da empresa: {pessoa_juridica.dataAberturaEmpresa}")
print(f"CNPJ: {pessoa_juridica.cnpj}")

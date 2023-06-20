class Main:
    pass

from Cliente import Cliente

from Conta import Conta

c1= Cliente("João", "114444-2222")
conta=Conta(c1.get_nome(), 1222)

conta.deposita(100)
conta.saque(50)
conta.extrato()

print(c1)
print(c1.nome, " e ", c1._telefone)
print(conta._titular, "Numero: \n", conta.numero, ". Seu saldo é: \n", conta.saldo, "O valor depositado foi: \n", conta.deposito, "O valor sacado foi: ", conta.saque, "Seu Extrato atual é: \n", conta.extrato())
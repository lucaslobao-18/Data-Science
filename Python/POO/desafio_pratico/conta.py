class ContaBancaria:
    titular = "usuario"
    saldo = 0

    #METODO CONSTRUTOR
    def __init__(self,nome,valor):
        self.titular = nome
        self.saldo = valor

    #METODOS
    def depositar(self,valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, saque):
        if self.saldo >= saque:
            self.saldo -= saque
            return self.saldo
        else:
            print("Saldo Insulficiente")
            return self.saldo
        
    def exibir_saldo(self):
        return self.saldo
#Por padrão, nome de classe começa com letra maiúscula
class Pessoa:
    #atributos
    __nome = "Marcio" #os 2 underlines especificam que o atributo só pode ser acessado pela própria classe
    idade = 45

    #metodos
    def exibir(self,nome,idade):
        print(nome,idade)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(self.nome, self.idade)

    #GETTERS E SETTERS
    @property #permite que eu altere propriedades padrão da estrutura do python
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

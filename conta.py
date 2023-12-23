class Conta:
    def __init__(self,numero, titular, saldo, limite): #função construtora/posso passar um parâmetro opcional também para esses parâmetros
        print(f'Construindo objeto...{self}')#Self é a referência que onde encontrar o objeto, vai ser caminho para ir para cada objeto e forma distinta
        # Abributos
        self.__numero = numero #colocando esses dois underscore o atributo fica privado é equivalente ao private no java porém tem que alterar em todos os métodos pois agora faz parte do nome da variável
        self.__titular = titular #poded chamar usando por exemplo conta._Conta__saldo (<objeto>._<classe>__<atributo>) e fica oculto na recomendação
        self.__saldo = saldo
        self.__limite = limite
    #Criando métodos
    def extrato(self):
        print(f'Titular: {self.__titular}')
        print(f'Saldo: {self.__saldo}')

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino): #Se colocar o __ antes do método pode criar um método privado como __transfere  por exemplo
        #Encapsulamento
        self.saca(valor) #Como a origem acessa o mesmo endereço do self pois é o objeto que chama a função, entçao vou tirar p parâmetro origem da função e para chamar o método saca vou usar o self
        destino.deposita(valor)

    #Método para retornar os atributos agora privados/Getters- sempre retorna
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    #Setters - nunca retorna, só altera os elementos
    def limite(self, limite):
        self.__limite = limite
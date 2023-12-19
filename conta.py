class Conta:
    def __init__(self,numero, titular, saldo, limite): #função construtora/posso passar um parâmetro opcional também para esses parâmetros
        print(f'Construindo objeto...{self}')#Self é a referência que onde encontrar o objeto, vai ser caminho para ir para cada objeto e forma distinta
        # Instanciando objetos
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
class Calculadora:
    def __init__(self):
        pass
    def soma(self, a, b):
        return a + b

    def subtracao(self, a ,b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b
        
if __name__ == '__main__':
    calculadora = Calculadora()
    print(calculadora.soma(1,2))
    print(calculadora.subtracao(4,2))
    print(calculadora.multiplicacao(10,2))
    print(calculadora.divisao(2,1))
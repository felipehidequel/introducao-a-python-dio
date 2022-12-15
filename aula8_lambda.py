contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorrao', 'gatinho']
zap = contador_letras(lista_animais)
print(zap)

# soma = lambda a,b: a + b
# subtracao = lambda a, b: a - b

# print(soma(1,1))
# print(subtracao(3,1))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,

}

soma = calculadora['soma']
print(soma(10, 5))
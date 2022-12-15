lista = [12, 10 , 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

## tuplas são imutaveis; os valores não podem ser alterados
tupla = (1, 10, 12, 14)
print(len(tupla)) ## quantos elementos tem na tupla
tupla_animal = tuple(lista_animal)
print(tupla_animal)
lista_numerica = list(tupla)
print(lista_numerica)


# print(lista_animal[1])
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

# print(sum(lista))
# print(max(lista))
# print(min(lista))
# print(min(lista_animal))
# print(max(lista_animal))

# if 'lobo' in lista_animal:
#     print('existe lobo na lista')
# else:
#     print('não existe lobo na lista. Será incluido')
#     lista_animal.append('lobo')
#     print(lista_animal)

#lista_animal.pop(0)
# lista_animal.remove('elefante')
# print(lista_animal)

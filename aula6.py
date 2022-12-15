conjunto = {1, 2 , 3 , 4 ,5}
conjunto2= {5, 6 , 7 , 8}

conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)
conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao)
conjunto_diferenca = conjunto.difference(conjunto2)
print(conjunto_diferenca)
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print(f"diferença simetrica: {conjunto_diff_simetrica}")

conjunto_a = {1, 2, 3,}
conjunto_b = {1, 2, 3 , 4, 5, 6}
print(conjunto_a.issubset(conjunto_b)) 
print(conjunto_b.issuperset(conjunto_a))

lista = ['cachorro', 'cachorro', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)

# conjunto = {1, 2, 3 , 4, 4, 2}
# conjunto.add(5)
# conjunto.discard(5)
# print(conjunto)
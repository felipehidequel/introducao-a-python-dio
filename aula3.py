a = int(input('primeiro bimestre: '))
while a > 10:
    a = int(input('entrada invalida: '))
b = int(input('segundo bimestre: '))
while b > 10:
    b = int(input('entrada invalida: '))
c = int(input('terceiro bimestre: '))
while c > 10:
    c = int(input('entrada invalida: '))
d = int(input('quarto bimestre: '))
while d > 10:
    d = int(input('entrada invalida: '))
media = (a + b + c + d) / 4
print(f'media: {media}')
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print(f'media: {media}')
# else:
#     print('entrada invalida!')

# a = int(input('Entre com um valor: '))
# b = int(input('Entre com um segundo valor valor: '))
# resto_a = a%2
# resto_b = b%2
# if resto_a == 0 or resto_b == 0:
#     print('foi digitado um numero par')
# else:
#     print('nenhum valor par')

# a = int(input('primeiro valor: '))
# b = int(input('segundo valor: '))
# c = int(input('Terceiro Valor: '))
# if a > b and a>c:
#     print(f'o maior numero é {a}')
# elif b>a and b>c:
#     print(f'o maior numero é {b}')
# else:
#     print(f'o maior numero é {c}')
# print('final do progama')

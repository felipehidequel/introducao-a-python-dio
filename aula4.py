nota = int(input('entre com a nota: '))
while nota > 10:
    print('nota invalida!')
    nota = nota = int(input('entre com a nota: '))


# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# # Imprime valores primos de 0 ate o numero informado
# a = int(input('entre com um valor: '))
# for i in range(a+1):
#     div = 0
#     for x in range(1, i+1):
#         resto = i % x
#         if resto == 0:
#             div += 1

#     if div == 2:
#         print(f"O numero {i} é primo")
    
# a = int(input('entre com um numero: '))

# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     if resto == 0:
#         div += 1

# if div == 2:
#     print(f"O numero {a} é primo")
# else:
#     print(f'O numero {a} não é primo')
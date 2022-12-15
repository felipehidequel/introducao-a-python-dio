
lista = [1, 10]
arquivo = open('Notas.txt', 'r')
try:
    divisao = 10/0
    numero = lista[1]
    
except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por zero')
except IndexError:
    print('Erro ao acessar um indice invalido da lista')
except BaseException as ex:
    print(f'erro desconhecido. {ex}')
finally:
    print("Sempre executa")
    print('fechando arquivo')
    arquivo.close()
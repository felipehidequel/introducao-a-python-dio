import shutil

def escrever_arquivo(texto):
    diretorio = '/mnt/c/Users/felip/Documents/introdução a python - dio/app_python/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas])/4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):    
    shutil.copy(nome_arquivo, '/mnt/c/Users/felip/Desktop')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '/mnt/c/Users/felip/Desktop')

if __name__ == '__main__':
    pass
    # move_arquivo('teste.txt')
    # copia_arquivo('Notas.txt')
    # lista_media = media_notas('Notas.txt')
    # print(lista_media)
    #escrever_arquivo('Primeira Linha.\n')
    # aluno = '\nCeasr, 6, 3, 7, 6'
    # atualizar_arquivo('Notas.txt', aluno)
    #ler_arquivo('Teste.txt')
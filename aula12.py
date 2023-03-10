import requests

def retorna_dados_cep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    print(response.status_code)
    print(response.json())
    print(type(response.json()))
    dados_cep = response.json()
    print(dados_cep['cep'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://pokeapi.co')
    print(response)
    # retorna_dados_cep('59965000')
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon['sprites']['front_shiny'])
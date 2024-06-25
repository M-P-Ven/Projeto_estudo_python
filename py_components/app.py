import requests
import json

def Criar_pokedex():
    '''esta função faz repetidamente requisições a PokeAPI e pega dados especificos de cada entrada pra criar uma pokedex com menos informações
    INPUTS:
        ---
    OUTPUTS:
        - um arquivo JSON com a nationaldex 
    
    '''
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    pokedex = {}
    if response.status_code == 200:
        counter = 1
        while response.status_code == 200:
            urlpkmn = f'https://pokeapi.co/api/v2/pokemon/{counter}/'
            response = requests.get(urlpkmn)
            dados_json = response.json()
            id_pokemon = dados_json['name']
            pokedex[id_pokemon] = []
            pokedex[id_pokemon].append({
            "numero_dex" : dados_json['id'],
            "nome" : dados_json['name'],
            "altura" : dados_json['height'],
            "peso" : dados_json['weight'],
            "tipagem" : dados_json['types']
            })
            counter += 1
    else:
        print(f'{response.status_code} - {response.text}')
    nome_do_arquivo = 'pokedex.json'
    with open(nome_do_arquivo, 'w') as arquivo_dex:
            json.dump(pokedex, arquivo_dex, indent=4)

def Criar_pokedex_number_filter(number):
    '''esta função faz uma requisição a PokeAPI e pega dados especificos de um pokemon e retorna a entrada dele na dex
    INPUTS:
        - o numero do pokemon requisitado
    OUTPUTS:
        - uma lista com a entrada daquele pokemon. 
    '''
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    if response.status_code == 200:
        counter = 1
        while response.status_code == 200:
            urlpkmn = f'https://pokeapi.co/api/v2/pokemon/{number}/'
            response = requests.get(urlpkmn)
            dados_json = response.json()
            pokemon = []
            pokemon.append({
            "numero_dex" : dados_json['id'],
            "nome" : dados_json['name'],
            "altura" : dados_json['height'],
            "peso" : dados_json['weight'],
            "tipagem" : dados_json['types']
            })
            counter += 1
            return pokemon
    else:
        print(f'{response.status_code} - {response.text}')

def dex_entry(number):
    '''esta função faz uma requisição a PokeAPI e pega dados especificos de um pokemon e retorna a entrada dele na dex
    INPUTS:
        - o numero do pokemon requisitado
    OUTPUTS:
        -um arquivo JSON com a entrada do pokemon indicado pelo numero 
    '''
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    pokedex = {}
    if response.status_code == 200:
        urlpkmn = f'https://pokeapi.co/api/v2/pokemon/{number}/'
        response = requests.get(urlpkmn)
        dados_json = response.json()
        id_pokemon = dados_json['name']
        pokedex[id_pokemon] = []
        pokedex[id_pokemon].append({
        "numero_dex" : dados_json['id'],
        "nome" : dados_json['name'],
        "altura" : dados_json['height'],
        "peso" : dados_json['weight'],
        "tipagem" : dados_json['types']
        })
        counter += 1
    else:
        print(f'{response.status_code} - {response.text}')
    nome_do_arquivo = f'pokedex_entry_number_{number}.json'
    with open(nome_do_arquivo, 'w') as arquivo_dex:
            json.dump(pokedex, arquivo_dex, indent=4)
    
def Criar_pokedex_regiao(generation):
    '''esta função chama repetidamente a função Criar_pokedex_number_filter(), passando por todos os pokemon de uma geração especifica e criando um arquivo com essas entradas.
    gen 1: 1-151
    gen 2: 152-251
    gen 3:252-386
    gen 4:387-493
    gen 5:494-649
    gen 6:650-721
    gen 7:722-809
    gen 8:810-905
    gen 9:906-1025
    INPUTS
        - o numero da geração desejada
    OUTPUTS: 
        - um arquivo JSON com a dex daquela geração 
    '''
    gen = generation
    match gen:
         case 1:
            counter = 1
            pokedex = {}
            while counter < 152:
                pokedex[counter].append(Criar_pokedex_number_filter(counter))
            nome_do_arquivo = f'pokedex_Kanto_(gen{gen}).json'
            with open(nome_do_arquivo, 'w') as arquivo_dex:
                    json.dump(pokedex, arquivo_dex, indent=4)

         case 2:
            counter = 152
            pokedex = {}
            while counter < 252:
                pokedex[counter].append(Criar_pokedex_number_filter(counter))
            nome_do_arquivo = f'pokedex_Jotho_(gen{gen}).json'
            with open(nome_do_arquivo, 'w') as arquivo_dex:
                    json.dump(pokedex, arquivo_dex, indent=4)
         
         case 3:
            counter = 252
            pokedex = {}
            while counter < 387:
                pokedex[counter].append(Criar_pokedex_number_filter(counter))
            nome_do_arquivo = f'pokedex_Hoenn_(gen{gen}).json'
            with open(nome_do_arquivo, 'w') as arquivo_dex:
                    json.dump(pokedex, arquivo_dex, indent=4)
         
         case 4:
            counter = 387
            pokedex = {}
            while counter < 494:
                pokedex[counter].append(Criar_pokedex_number_filter(counter))
            nome_do_arquivo = f'pokedex_Sinnoh_(gen{gen}).json'
            with open(nome_do_arquivo, 'w') as arquivo_dex:
                    json.dump(pokedex, arquivo_dex, indent=4)
         
         case 5:
            counter = 494
            pokedex = {}
            while counter < 650:
                pokedex[counter].append(Criar_pokedex_number_filter(counter))
            nome_do_arquivo = f'pokedex_Unova_(gen{gen}).json'
            with open(nome_do_arquivo, 'w') as arquivo_dex:
                    json.dump(pokedex, arquivo_dex, indent=4)

         case 6:
            counter = 650
            pokedex = {}
            while counter < 722:
                pokedex[counter].append(Criar_pokedex_number_filter(counter))
            nome_do_arquivo = f'pokedex_Kalos_(gen{gen}).json'
            with open(nome_do_arquivo, 'w') as arquivo_dex:
                    json.dump(pokedex, arquivo_dex, indent=4)
         
         case 7:
            counter = 722
            pokedex = {}
            while counter < 810:
                pokedex[counter].append(Criar_pokedex_number_filter(counter))
            nome_do_arquivo = f'pokedex_Alola_(gen{gen}).json'
            with open(nome_do_arquivo, 'w') as arquivo_dex:
                    json.dump(pokedex, arquivo_dex, indent=4)
         
         case 8:
            counter = 810
            pokedex = {}
            while counter < 906:
                pokedex[counter].append(Criar_pokedex_number_filter(counter))
            nome_do_arquivo = f'pokedex_Galar_(gen{gen}).json'
            with open(nome_do_arquivo, 'w') as arquivo_dex:
                    json.dump(pokedex, arquivo_dex, indent=4)
         
         case 9:
            counter = 906
            pokedex = {}
            while counter < 1026:
                pokedex[counter].append(Criar_pokedex_number_filter(counter))
            nome_do_arquivo = f'pokedex_Paldea_(gen{gen}).json'
            with open(nome_do_arquivo, 'w') as arquivo_dex:
                    json.dump(pokedex, arquivo_dex, indent=4)
         
         case _:
            print('numero invalido')

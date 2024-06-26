import requests
import json
import os

def Criar_pokedex():
    '''esta função faz repetidamente requisições a PokeAPI e pega dados especificos de cada entrada pra criar uma pokedex com menos informações
    INPUTS:
        ---
    OUTPUTS:
        - um arquivo JSON com a nationaldex 
    
    '''
    nome_do_arquivo = 'pokedex.json'
    arquivo_esitente = os.path.exists(nome_do_arquivo)
    if arquivo_esitente == False:
        number = 1
        number_limit = 3
        url = 'https://pokeapi.co/api/v2/pokemon/'
        response = requests.get(url)
        pokedex = {}
        if response.status_code == 200:
            while number < number_limit:
                urlpkmn = f'https://pokeapi.co/api/v2/pokemon/{number}/'
                response_pkmn = requests.get(urlpkmn)
                if response_pkmn.status_code == 200:
                    dados_json = response_pkmn.json()
                    id_pokemon = dados_json['name']
                    pokedex[id_pokemon] = []
                    pokedex[id_pokemon].append({
                    "numero_dex" : dados_json['id'],
                    "nome" : dados_json['name'],
                    "altura" : dados_json['height'],
                    "peso" : dados_json['weight'],
                    "tipagem" : dados_json['types']
                    })
                    number += 1
                    number_limit +=1
                else:
                    number_limit = 0
                        
        else:
            print(f'{response.status_code} - {response.text}')

        with open(nome_do_arquivo, 'w') as arquivo_dex:
                json.dump(pokedex, arquivo_dex, indent=4)  
        return 'arquivo_criado'
    else:
         return 'arquivo_ja_existe'

def dex_entry(number):
    '''esta função faz uma requisição a PokeAPI e pega dados especificos de um pokemon e retorna a entrada dele na dex
    INPUTS:
        - o numero do pokemon requisitado
    OUTPUTS:
        -um arquivo JSON com a entrada do pokemon indicado pelo numero 
    '''
    nome_do_arquivo = f'pokedex_entry_number_{number}.json'
    arquivo_esitente = os.path.exists(nome_do_arquivo)
    if arquivo_esitente == False:
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
        else:
            print(f'{response.status_code} - {response.text}')
        with open(nome_do_arquivo, 'w') as arquivo_dex:
                json.dump(pokedex, arquivo_dex, indent=4)
        return 'arquivo_criado'
    else:
         return 'arquivo_ja_existe'

def Criar_pokedex_number_filter(number, number_limit):
    '''esta função faz uma requisição a PokeAPI e pega dados especificos de um pokemon e retorna a entrada dele na dex
    INPUTS:
        - o numero do pokemon requisitado
    OUTPUTS:
        - uma lista com a entrada daquele pokemon. 
    '''
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    pokedex = {}
    if response.status_code == 200:
        while number < number_limit:
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
            number += 1
    else:
        print(f'{response.status_code} - {response.text}')

    return pokedex
        
def Criar_pokedex_regiao(generation):
    '''esta função chama repetidamente a função Criar_pokedex_number_filter(), passando por todos os pokemon de uma geração especifica e criando um arquivo com essas entradas.
    gen 1: Kanto 1-151
    gen 2: Johto 152-251
    gen 3: Hoenn 252-386
    gen 4: Sinnoh 387-493
    gen 5: Unova 494-649
    gen 6: Kalos 650-721
    gen 7: Alola 722-809
    gen 8: Galar 810-905
    gen 9: Paldea 906-1025
    INPUTS
        - o numero da geração desejada
    OUTPUTS: 
        - um arquivo JSON com a dex daquela geração 
    '''
    gen = generation
    match gen:
         case '1':
            nome_do_arquivo = f'pokedex_Kanto_(gen{gen}).json'
            arquivo_esitente = os.path.exists(nome_do_arquivo)
            if arquivo_esitente == False:
                number = 1
                number_limit = 152
                pokedex_gen = Criar_pokedex_number_filter(number, number_limit)
                with open(nome_do_arquivo, 'w') as arquivo_dex:
                        json.dump(pokedex_gen, arquivo_dex, indent=4)
                return 'arquivo_criado'
            else:
                return 'arquivo_ja_existe'

         case '2':
            nome_do_arquivo = f'pokedex_Johto_(gen{gen}).json'
            arquivo_esitente = os.path.exists(nome_do_arquivo)
            if arquivo_esitente == False:
                number = 152
                number_limit = 252
                pokedex_gen = Criar_pokedex_number_filter(number, number_limit)
                with open(nome_do_arquivo, 'w') as arquivo_dex:
                        json.dump(pokedex_gen, arquivo_dex, indent=4)
                return 'arquivo_criado'
            else:
                return 'arquivo_ja_existe'
         
         case '3':
            nome_do_arquivo = f'pokedex_Hoenn_(gen{gen}).json'
            arquivo_esitente = os.path.exists(nome_do_arquivo)
            if arquivo_esitente == False:
                number = 252
                number_limit = 387
                pokedex_gen = Criar_pokedex_number_filter(number, number_limit)
                with open(nome_do_arquivo, 'w') as arquivo_dex:
                        json.dump(pokedex_gen, arquivo_dex, indent=4)
                return 'arquivo_criado'
            else:
                return 'arquivo_ja_existe'
         
         case '4':
            nome_do_arquivo = f'pokedex_Sinnoh_(gen{gen}).json'
            arquivo_esitente = os.path.exists(nome_do_arquivo)
            if arquivo_esitente == False:
                number = 387
                number_limit = 494
                pokedex_gen = Criar_pokedex_number_filter(number, number_limit)
                with open(nome_do_arquivo, 'w') as arquivo_dex:
                        json.dump(pokedex_gen, arquivo_dex, indent=4)
                return 'arquivo_criado'
            else:
                return 'arquivo_ja_existe'
         
         case '5':
            nome_do_arquivo = f'pokedex_Unova_(gen{gen}).json'
            arquivo_esitente = os.path.exists(nome_do_arquivo)
            if arquivo_esitente == False:
                number = 494
                number_limit = 650
                pokedex_gen = Criar_pokedex_number_filter(number, number_limit)
                with open(nome_do_arquivo, 'w') as arquivo_dex:
                        json.dump(pokedex_gen, arquivo_dex, indent=4)
                return 'arquivo_criado'
            else:
                return 'arquivo_ja_existe'

         case '6':
            nome_do_arquivo = f'pokedex_Kalos_(gen{gen}).json'
            arquivo_esitente = os.path.exists(nome_do_arquivo)
            if arquivo_esitente == False:
                number = 650
                number_limit = 722
                pokedex_gen = Criar_pokedex_number_filter(number, number_limit)
                with open(nome_do_arquivo, 'w') as arquivo_dex:
                        json.dump(pokedex_gen, arquivo_dex, indent=4)
                return 'arquivo_criado'
            else:
                return 'arquivo_ja_existe'
         
         case '7':
            nome_do_arquivo = f'pokedex_Alola_(gen{gen}).json'
            arquivo_esitente = os.path.exists(nome_do_arquivo)
            if arquivo_esitente == False:
                number = 722
                number_limit = 810
                pokedex_gen = Criar_pokedex_number_filter(number, number_limit)
                with open(nome_do_arquivo, 'w') as arquivo_dex:
                        json.dump(pokedex_gen, arquivo_dex, indent=4)
                return 'arquivo_criado'
            else:
                return 'arquivo_ja_existe'
         
         case '8':
            nome_do_arquivo = f'pokedex_Galar_(gen{gen}).json'
            arquivo_esitente = os.path.exists(nome_do_arquivo)
            if arquivo_esitente == False:
                number = 810
                number_limit = 906
                pokedex_gen = Criar_pokedex_number_filter(number, number_limit)
                with open(nome_do_arquivo, 'w') as arquivo_dex:
                        json.dump(pokedex_gen, arquivo_dex, indent=4)
                return 'arquivo_criado'
            else:
                return 'arquivo_ja_existe'
         
         case '9':
            nome_do_arquivo = f'pokedex_Paldea_(gen{gen}).json'
            arquivo_esitente = os.path.exists(nome_do_arquivo)
            if arquivo_esitente == False:
                number = 906
                number_limit = 1026
                pokedex_gen = Criar_pokedex_number_filter(number, number_limit)
                with open(nome_do_arquivo, 'w') as arquivo_dex:
                        json.dump(pokedex_gen, arquivo_dex, indent=4)
                return 'arquivo_criado'
            else:
                return 'arquivo_ja_existe'
         
         case _:
            print('numero invalido')

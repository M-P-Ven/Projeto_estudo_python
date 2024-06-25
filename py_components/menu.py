from py_components.app import *

def txt_decoration(texto):
    print('*'*(len(texto)+ 4))
    print(f'\n{texto.center(2, '-')}\n')
    print('*'*(len(texto)+ 4))  

def arquivo_criado():
    txt_decoration('arquivo criado, por favor verifique sua pasta.')  

def menu():
    txt_decoration('ℙ𝕆𝕂𝔼𝔻𝔼𝕏.𝕁𝕊𝕆ℕ')
    print('opções:\n 1: complete pokedex\n2: gen dex entry \n3: pokemon specific dex entry\n4: sair\n')
    selecao()


def selecao():
    '''parte do menu onde ocorre a seleção de que tipo de arquivo o usuario quer
    INPUT:
        - o numero da opção selecionada
    OUTPUT:
        - o arquivo requisitado
    '''
    escolha = input()
    match escolha:
        case 1:
            Criar_pokedex()
            arquivo_criado()
            menu()
        case 2:
            pokemon = input('insira o numero do pokemon que deseja: ')
            dex_entry(pokemon)
            arquivo_criado()
            menu()
        case 3:
            gen = input('opções:\n1:Kanto(1-151)\n2:Jotho(152-251)\n3:Hoenn(252-386)\n4:Sinnoh(387-493)\n5:Unova(494-649)\n6:Kalos(650-721)\n7:Alola(722-809)\n8:Galar(810-905)\n9:Paldea(906-1025)\n') 
            Criar_pokedex_regiao(gen)
            arquivo_criado()
            menu()
        case 4:
            print('Bye!')
        case _:
            print('por favor, ensira o numero da opção solicitada')
            menu()
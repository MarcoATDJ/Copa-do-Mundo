import os


def arquivo_existe(arquivo_nome):
    try:
        arquivo = open(arquivo_nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criar_arquivo(arquivo_nome):
    try:
        arquivo = open(arquivo_nome, 'wt+')
        arquivo.close()
    except:
        print('ERRO ao abrir o arquivo!')
    else:
        print(f'Arquivo {arquivo_nome} criado com sucesso!')
        

def ler_jogador(arquivo_nome):
    try:
        arquivo = open(arquivo_nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        linhas = arquivo.readlines()
        ultimo_nome = linhas[len(linhas)-1]
        print(ultimo_nome)
        return ultimo_nome
        


def add_jogador_arq(arquivo_nome, nome=''):
    try:
        arquivo = open(arquivo_nome, 'at')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        try:
            arquivo.write(f'\n{nome}')
        except:
            print('ERRO ao registrar jogador!')
        else:
            print(f'Novo registro de {nome} cadastrado.')
            arquivo.close()
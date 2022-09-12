import os
import players
import dao_game

class main():
    
    opc = None   
    list = ['Jogar - Copa do Mundo', 'Sair da Partida']
    
    dados = dao_game.ConsultarSelecao()
    dados.abrir_csv('data\\selecoes.csv')
    dados.printar_csv()
    
    arquivo = 'lista_jogadores.txt'
    if not players.arquivo_existe(arquivo):
        players.criar_arquivo(arquivo)
    
    
    while opc != 2:
        #print(os.system("cls"))  
        print('-'*42)
        txt = 'COPA DO MUNDO 2022'
        print(txt.center(42))
        print('-'*42)
        cont = 1
        for item in list:
            print(f'{cont} - {item}')
            cont+=1
        print('-'*42)
        opc = int(input(print('Digite sua opção: ')))
        if opc == 1:
            nome = str(input("Escreva seu nome: "))
            players.add_jogador_arq(arquivo, nome.upper())
            selecao = str(input("Digite o nome da Seleção: "))
            dados.consultar_linha(selecao.upper())
        elif opc == 2:
            ultimo_nome = players.ler_jogador(arquivo)
            print (f'Obrigado {ultimo_nome} por jogar!')
        else:
            print('ERRO! Digite uma opção válida!')
            break 
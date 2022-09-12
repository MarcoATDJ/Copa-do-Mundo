import pandas as pd


class ConsultarSelecao():
    
    dados = None
    nome_linha = None    
    
    def abrir_csv(self, csv_file):
        try:
            self.dados = pd.read_csv(csv_file, sep=",",encoding="utf8")
        except:
            print(f"O arquivo CSV não foi aberto com sucesso!")
            return False
        else:
            print(f"O arquivo CSV foi aberto com sucesso")
            return True
        
    def printar_csv(self):
        print(self.dados)
            
    def consultar_linha(self, nome_selecao):
            if nome_selecao in str(self.dados["Seleção"].str.upper()):
                print(f'Seleção existe')
                indice = self.dados.index[self.dados["Seleção"].str.upper() == nome_selecao].to_list()
                aux = indice[0]
                print(aux)
                return aux
            else:
                print(f'Seleção não existe!')
                aux = -1
                return aux
                
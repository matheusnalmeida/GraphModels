from Buscas.caminho import Caminho
from Exceptions.CaminhoExistenteException import CaminhoExistenteException
from Exceptions.CaminhoInexistenteException import CaminhoInexistenteException
#Classe responsavel por armazenar as possiveis solucoes(caminhos) para os algoritimos de busca
class Fronteira:

    def __init__(self):
        self.__possiveis_caminhos = {}

    def add_caminho(self,caminho :Caminho):
        if caminho.vertice_final.id not in self.__possiveis_caminhos:
            self.__possiveis_caminhos[caminho.vertice_final.id] = caminho
            return
        
        raise CaminhoExistenteException("Ja existe um caminho com o vertice final salvo na fronteira", caminho)
            
    def remove_caminho(self, caminho :Caminho):
        if caminho.vertice_final.id in self.__possiveis_caminhos:
            del self.__possiveis_caminhos[caminho.vertice_final.id]

    def add_caminhos(self, vetorDeCaminhos :list):
        for caminho in vetorDeCaminhos:
            self.add_caminho(caminho)
    
    def retorna_caminho(self,caminho :Caminho):
        for caminhoId in self.possiveis_caminhos:
            if caminhoId == caminho.vertice_final.id:
                return self.possiveis_caminhos[caminhoId]

        raise CaminhoInexistenteException("Não existe caminho com o vertice final passado como parametro na fronteira",caminho)
        
    #Verifica se a fronteira esta sem caminhos salvos
    def fronteira_vazia(self):
        return len(self.__possiveis_caminhos) == 0

    @property
    def possiveis_caminhos(self):
        return self.__possiveis_caminhos
from Graph.aresta import Aresta
from Graph.vertice import Vertice
from Util.util import Util
from Exceptions.VerticeInexistenteException import VerticeInexistenteException
from Exceptions.HeuristicaException import HeuristicaException
from Exceptions.CaminhoInexistenteException import CaminhoInexistenteException
#----------------- Busca Importacao ---------------------------
from Buscas.caminho import Caminho
from Buscas.fronteira import Fronteira

class Grafo:

    def __init__(self,verticesPreCriados :list = [],orientado :bool = False):
        self.__orientado = orientado
        self.__vertices = verticesPreCriados
        self.__numero_de_vertices = len(verticesPreCriados)
        
    def add_vertice(self, vertice :Vertice):
        self.vertices.append(vertice)
        self.numero_de_vertices+=1
    
    def remover_vertice(self, vertice: Vertice):
        vertice_procurado = self.procurarVertice(vertice)
        if not vertice_procurado:
            raise VerticeInexistenteException("O vertice informado para remoção nao existe",[vertice])
        vertice_procurado.remover_arestas_entrada()
        self.vertices.remove(vertice_procurado)
        self.numero_de_vertices-=1

    def add_aresta(self,aresta :Aresta):
        vertice_procurado_inicio = self.procurarVertice(aresta.vertice_inicio)
        vertice_procurado_fim = self.procurarVertice(aresta.vertice_fim)
        if vertice_procurado_inicio and vertice_procurado_fim:
            arestaNova = Aresta(vertice_procurado_inicio,vertice_procurado_fim,aresta.peso,aresta.id)
            vertice_procurado_inicio.add_aresta(arestaNova)
            if not self.orientado:
                vertice_procurado_fim.add_aresta(Util.inverterSentidoArestas(arestaNova))
        else:
            raise VerticeInexistenteException("Foram inseridos vertices inexistentes na aresta a ser adicionada no grafo",
                                            [vertice_procurado_inicio,vertice_procurado_fim])

    def remover_aresta(self,aresta :Aresta):
        vertice_procurado_inicio = self.procurarVertice(aresta.vertice_inicio)
        vertice_procurado_fim = self.procurarVertice(aresta.vertice_fim)
        if vertice_procurado_inicio and vertice_procurado_fim:
            vertice_procurado_inicio.remove_aresta(aresta)
            if not self.orientado:
                vertice_procurado_fim.remove_aresta(Util.inverterSentidoArestas(aresta))
        else:
            raise VerticeInexistenteException("Foram inseridos vertices inexistentes na aresta a ser removida do grafo",
                                            [vertice_procurado_inicio,vertice_procurado_fim])  

    def atualiza_heuristica(self,vertice :Vertice, novoValorHeuristica):
        vertice_procurado = self.procurarVertice(vertice)
        if vertice_procurado:
            vertice_procurado.heuristica = novoValorHeuristica
            return
        raise VerticeInexistenteException("Foi informado um vertice inexistente no grafo para atualização da heuristica",[vertice])

    def procurarVertice(self, vertice_procurado: Vertice):
        for vertice in self.vertices:
            if vertice_procurado == vertice:
                return vertice

    #---------------------------------------------- Algoritimos de busca ------------------------------------------------------
    def buscaCustoUniforme(self,verticeInicio :Vertice,verticeDestino :Vertice):
        verticeVisitados = []
        menoresCaminhosEncontrados = []
        verticeInicio = self.procurarVertice(verticeInicio)
        if not verticeInicio:
            raise VerticeInexistenteException("Foi informado um vertice de inicio que não existe no grafo. Não foi possivel realizar a busca de custo uniforme.",
                            [verticeInicio]) 
        fronteira = Fronteira()
        fronteira.add_caminho(Caminho(verticeInicio))
        
        while (not fronteira.fronteira_vazia()):
            menorCaminhoAtual = Util.retorna_menor_caminho_fronteira_por_distancia(fronteira)
            fronteira.remove_caminho(menorCaminhoAtual)
            if menorCaminhoAtual.vertice_final == verticeDestino:
                return Util.montar_mensagem_busca_custo_uniforme(verticeInicio,verticeDestino,[menorCaminhoAtual])
            if menorCaminhoAtual.distancia != 0:
                menoresCaminhosEncontrados.append(menorCaminhoAtual)
            verticeVisitados.append(menorCaminhoAtual.vertice_final)
            caminhosNaoVisitados = Util.retorna_menor_caminhos_nao_visitados_por_peso(menorCaminhoAtual,verticeVisitados)
            #Verificando se existe algum caminho na fronteira que possui vertice final igual a algum dos novos caminhos nao visitados
            for caminho in caminhosNaoVisitados:
                try:
                    caminhoFronteira = fronteira.retorna_caminho(caminho) 
                    # Caso ja exista na fronteira um caminho que possua vertice final igual ao caminho atual,
                    # somente sera substituido se possuir uma distancia menor do que o ja existente 
                    if caminho.distancia < caminhoFronteira.distancia:
                        fronteira.remove_caminho(caminhoFronteira)
                        fronteira.add_caminho(caminho)
                except CaminhoInexistenteException:
                    fronteira.add_caminho(caminho)
        
        return Util.montar_mensagem_busca_custo_uniforme(verticeInicio,verticeDestino,menoresCaminhosEncontrados)

    def buscaGulosa(self, verticeInicio :Vertice, verticeDestino :Vertice):
        heuristicasNaoValidas = Util.grafo_sem_eurisitica(self)
        if heuristicasNaoValidas:
            raise HeuristicaException("Existem vertices no grafo com valor de heuristica invalido. Busca gulosa nao pode ser realizada")
        
        verticeInicio = self.procurarVertice(verticeInicio)
        if not verticeInicio:
            raise VerticeInexistenteException("Foi informado um vertice de inicio que não existe no grafo. Não foi possivel realizar a busca de custo uniforme.",
                            [verticeInicio]) 

        fronteira = Fronteira()
        fronteira.add_caminho(Caminho(verticeInicio))
        ultimoVerticeAtual = verticeInicio

        while (not fronteira.fronteira_vazia()):
            caminhoMenorHeuristica = fronteira.retorna_caminho(Caminho(ultimoVerticeAtual))
            print(caminhoMenorHeuristica)
            fronteira.remove_caminho(caminhoMenorHeuristica)
            if  caminhoMenorHeuristica.vertice_final == verticeDestino and caminhoMenorHeuristica.vertice_final.heuristica == 0:
                return Util.montar_mensagem_busca_gulosa(verticeInicio,verticeDestino,caminhoMenorHeuristica)
            novoCaminhoMenorHeuristica = Util.retorna_menor_caminho_por_heuristica(caminhoMenorHeuristica)
            if novoCaminhoMenorHeuristica:
                fronteira.add_caminho(novoCaminhoMenorHeuristica)
                ultimoVerticeAtual = novoCaminhoMenorHeuristica.vertice_final
        
        return Util.montar_mensagem_busca_gulosa(verticeInicio,verticeDestino)

    def buscaAEstrela(self):
        pass

    @property
    def vertices(self):
        return self.__vertices

    @vertices.setter
    def vertices(self,value):
        self.__vertices = value
    
    @property
    def numero_de_vertices(self):
        return self.__numero_de_vertices

    @numero_de_vertices.setter
    def numero_de_vertices(self,value):
        self.__numero_de_vertices = value
    
    @property
    def orientado(self):
        return self.__orientado

    @orientado.setter
    def orientado(self,value):
        self.__orientado = value
    
    def __str__(self):
        string_rep = ""
        for vertice in self.vertices:
            string_rep += "--------------------------------{0}--------------------------------------\n".format(vertice)
            for arestaId in vertice.arestas:
                arestasAtual = vertice.arestas[arestaId]
                for aresta in arestasAtual:
                    string_rep += "|_ Aresta de id {0} e esta entre os vertices {1} e {2}\n".format(aresta.id,aresta.vertice_inicio,aresta.vertice_fim)
        
        return string_rep

    
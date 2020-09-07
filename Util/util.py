from __future__ import annotations
import sys
from typing import TYPE_CHECKING
from Graph.aresta import Aresta
from Buscas.caminho import Caminho
from Buscas.fronteira import Fronteira 

if TYPE_CHECKING:
    from Graph.grafo import Grafo
    from Graph.vertice import Vertice

class Util():

    @staticmethod
    def inverterSentidoArestas(aresta :Aresta):
        arestaInvertida = Aresta(aresta.vertice_fim,aresta.vertice_inicio,aresta.peso)
        return arestaInvertida

    @staticmethod
    def retorna_aresta_entre_vertices(verticeInicio :Vertice,verticeFim :Vertice):
        for arestaId in verticeInicio.arestas:
            arestas = verticeInicio.arestas[arestaId]
            menorAresta = Aresta(None,None,peso=sys.maxsize)
            for aresta in arestas:
                if(aresta.peso <= menorAresta.peso):
                    menorAresta = aresta
            
            return menorAresta
    
    #Verifica se todos os vertices do grafo possuem um valor de eurisitca valido.
    #Retorna true caso existam vertices com heuristica invalida
    @staticmethod
    def grafo_sem_eurisitica(grafo :Grafo):
        for vertice in grafo.vertices:
            if vertice.heuristica < 0:
                return True
        return False

    #Retorna menor caminho de uma fronteira levando em consideracao a distancia
    @staticmethod
    def retorna_menor_caminho_fronteira_por_distancia(fronteira :Fronteira):
        menorCaminho = None
        for key in fronteira.possiveis_caminhos:
            caminho = fronteira.possiveis_caminhos[key]
            if not menorCaminho:
                menorCaminho = caminho
                continue

            if menorCaminho.distancia > caminho.distancia:
                menorCaminho = caminho

        return menorCaminho

    # Retorna os caminhos de menor distancia(lenvando em consideracao somente o peso) que levam a vertices ainda 
    # nao visitados e que continuam do caminho passado como parametro 
    @staticmethod
    def retorna_menor_caminhos_nao_visitados_por_peso(caminho :Caminho,vetorVerticesVisitados :list):
        caminhosNaoVisitados = []
        verticeFinal = caminho.vertice_final
        for arestaId in verticeFinal.arestas:
            arestasAtual = verticeFinal.arestas[arestaId]
            menorArestaAtual = None
            for aresta in arestasAtual:
                if aresta.vertice_fim not in vetorVerticesVisitados:
                    if not menorArestaAtual:
                        menorArestaAtual = aresta
                        continue
                                    
                    if menorArestaAtual.peso > aresta.peso:
                        menorArestaAtual = aresta

            if menorArestaAtual:
                novo_caminho = Caminho.init_caminho_pre_criado(caminho)
                novo_caminho.add_vertice(menorArestaAtual.vertice_fim,menorArestaAtual)    
                caminhosNaoVisitados.append(novo_caminho)    
        
        return caminhosNaoVisitados
    
    # Retorna o caminho de menor distancia(lenvando em consideracao somente a heuristica) que continuam do caminho passado como parametro   
    # Retorna nulo caso nao exista caminho de menor heuristica que o caminho atual  
    @staticmethod
    def retorna_menor_caminho_por_heuristica(caminho :CaminhoBuscaCustoUniforme):
        caminho_menor_heuristica = None
        # verticeMenorHeuristica ira armazenar o vertice que possui a menor heuristica 
        # dentro os vertices aos quais o ultimo vertice do caminho passado como parametro possui ligacao  
        verticeMenorHeuristica = None
        arestaVerticeMenorHeuristica = None
        verticeFinal = caminho.vertice_final
        for arestaId in verticeFinal.arestas:
            arestasAtual = verticeFinal.arestas[arestaId]
            if len(arestasAtual) != 0:
                arestaAtual =  arestasAtual[0]
                verticeAtual = arestasAtual[0].vertice_fim
                if not verticeMenorHeuristica:
                    verticeMenorHeuristica = verticeAtual
                    arestaVerticeMenorHeuristica = arestaAtual
                    continue
                if verticeMenorHeuristica.heuristica > verticeAtual.heuristica:
                    verticeMenorHeuristica = verticeAtual
                    arestaVerticeMenorHeuristica = arestaAtual
        
        # Caso o verticeMenorHeuristica for nulo,
        # isso significa que nao existe outro vertice de heuristica menor do que o ultimo vertice do caminho atual
        if not verticeMenorHeuristica or verticeMenorHeuristica.heuristica > verticeFinal.heuristica:
            return None
        
        novo_caminho = Caminho.init_caminho_pre_criado(caminho)
        novo_caminho.add_vertice(verticeMenorHeuristica,arestaVerticeMenorHeuristica)    

        return novo_caminho

    #Metodo utilizado para montar a mensagem de retorno da busca de custo uniforme
    @staticmethod
    def montar_mensagem_busca_custo_uniforme(verticeInicio :Vertice, verticeFim :Vertice, caminhos :list):
        if len(caminhos) == 0:
            return "Nao existe caminho entre os vertices {0} e {1}\n".format(str(verticeInicio),str(verticeFim))
        elif len(caminhos) == 1:
            return "O caminho de menor distancia entre os vertices {0} e {1}: \n" \
            "Distancia: {2} \nCaminho: {3}".format(str(verticeInicio),str(verticeFim),caminhos[0].distancia,caminhos[0])
        else:
            string_rep = "Nao existe caminho entre os vertices {0} e {1}\n Foram encontrados os seguintes caminhos :\n".format(str(verticeInicio),str(verticeFim))
            for caminho in caminhos:
                string_rep += "------------------------------------------------------------\n"
                string_rep += "Distancia: {0}\n Caminho: {1}\n".format(caminho.distancia,str(caminho))
            
            return string_rep

    #Metodo utilizado para montar a mensagem de retorno da busca gulosa
    @staticmethod
    def montar_mensagem_busca_gulosa(verticeInicio :Vertice, verticeFim :Vertice, caminho :ICaminho = None):
        if not caminho:
            return "Nao existe caminho entre os vertices {0} e {1}\nCaso exista um caminho, não foi possivel encontralo devido a possiveis valores invalidos de heuristica".format(str(verticeInicio),str(verticeFim))
        else:
            return "O caminho de menor distancia entre os vertices {0} e {1}: \n" \
            "Distancia: {2} \nCaminho: {3}".format(str(verticeInicio),str(verticeFim),caminho.distancia,caminho)

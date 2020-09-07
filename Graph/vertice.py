from __future__ import annotations
from typing import TYPE_CHECKING
from Exceptions import ArestaInexistenteException
from Util.util import Util

if TYPE_CHECKING:
    from Graph.aresta import Aresta

class Vertice:
    
    def __init__(self,id :str,heurisitica :int = -1):
        self.__id = id
        self.__heuristica = heurisitica
        self.__arestas = {}
        
    def add_aresta(self,aresta :Aresta):
        try:
            verticeFim = self.__arestas[aresta.vertice_fim.id]
            verticeFim.append(aresta)        
        except KeyError:
            self.__arestas[aresta.vertice_fim.id] = [aresta]
         
    def remove_aresta(self,aresta :Aresta):
        for verticeFim in self.__arestas:
            if(verticeFim == aresta.vertice_fim.id):
                arestas_verticeFim = self.__arestas[verticeFim]
                for arestaVerticeFim in arestas_verticeFim:
                    if (aresta.id == arestaVerticeFim.id):
                        arestas_verticeFim.remove(arestaVerticeFim)
                        if len(self.__arestas[verticeFim]) == 0:
                            del self.__arestas[verticeFim]
                        return
        raise ArestaInexistenteException("Não existe aresta que sai do vertice {0} ao vertice {1} com o id especificado".format(aresta.vertice_inicio,aresta.vertice_fim),
                                [aresta.vertice_inicio,aresta.vertice_fim])  

    #Remove as arestas de entrada no vertice atual
    def remover_arestas_entrada(self):
        for verticeId in self.arestas:
            arestasAtual = self.arestas[verticeId]
            for aresta in arestasAtual:
                try:
                    aresta.vertice_fim.remove_aresta(Util.inverterSentidoArestas(aresta))
                except Exception:
                    continue

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,value):
        self.__id = value

    @property
    def heurisitica(self):
        return self.__heurisitica
    
    @heurisitica.setter
    def heurisitica(self,value):
        self.__heurisitica = value
    
    @property
    def arestas(self):
        return self.__arestas

    def __eq__(self, other):
        if not isinstance(other, Vertice):
            return False
        
        if(self.id == other.id):
            return True

        return False

    def __str__(self):
        return self.id
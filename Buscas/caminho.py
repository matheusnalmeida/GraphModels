from __future__ import annotations
import sys
from typing import TYPE_CHECKING
from Graph.aresta import Aresta
from Exceptions.ArestasIncompatibilityException import ArestasIncompatibilityException
from Exceptions.VerticeInexistenteException import VerticeInexistenteException

if TYPE_CHECKING:
    from Graph.vertice import Vertice
    from Util.util import Util

#Classe responsavel por representar um dado caminho dos algoritimos de busca
class Caminho:

    def __init__(self,verticeInicio :Vertice = None):
        self.__distancia = 0 
        self.__arestas = []
        if not verticeInicio:
            self.__vertices = []
            return

        self.__vertices = [verticeInicio]
    
    #Retorna uma instancia de caminho criada previamente com mais de um vertice
    @classmethod
    def init_multiplos_vertices(cls, vertices :list, arestas: list):
        if(len(vertices) == 0 or (len(vertices) - 1) == len(arestas)):
            caminho = Caminho()
            for i in range(0,len(vertices)):
                if i == 0:
                    caminho.add_vertice(vertices[i],None)    
                    continue
                caminho.add_vertice(vertices[i],arestas[i-1])                                
            return caminho
        
        raise ArestasIncompatibilityException("A quantidade de aresta informadas nao é compativel com a quantidade de vertices")
        
    #Retorna uma instancia de caminho criada a partir de dados de outro caminho
    @classmethod
    def init_caminho_pre_criado(cls,caminho :Caminho):
        return Caminho.init_multiplos_vertices(caminho.vertices,caminho.arestas)

    # A aresta passada sera a ligacao do vertice anterior ao vertice que esta sendo inserido no momento.
    # Caso esse seja o primeiro vertice, o parametro de aresta nao sera necessario
    def add_vertice(self,vertice :Vertice,aresta :Aresta):
        if len(self.__vertices) == 0:
            self.__vertices.append(vertice)
            return

        if not aresta:
            raise ArestasIncompatibilityException ("É necessario passar a aresta como parametro a ser adicionada no caminho junto ao vertice")
        self.__vertices.append(vertice)
        self.__arestas.append(aresta)
        self.__distancia += aresta.peso

    def remove_ultimo_vertice(self):
        if len(self.__vertices) == 0:
            raise VerticeInexistenteException("Nao a vertices a serem removidos do caminho",[])
        elif len(self.__vertices) == 1:
            self.__vertices.remove(self.__vertices[-1])
            return
        
        self.__distancia -= self.__arestas[-1].peso
        self.__vertices.remove(self.__vertices[-1])
        self.__arestas.remove(self.__arestas[-1])

    @property
    def vertices(self):
        return self.__vertices

    @property
    def arestas(self):
        return self.__arestas

    @property
    def vertice_final(self):
        return self.__vertices[-1]

    @property
    def distancia(self):
        return self.__distancia
    
    def __str__(self):
        return '->'.join(str(vertice) for vertice in self.__vertices)

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Graph.vertice import Vertice

class Aresta:
    
    def __init__(self,vertice_inicio: Vertice,vertice_fim :Vertice,peso :int = 1,id :str = "default"):
        self.__id = id
        self.__vertice_inicio__ = vertice_inicio
        self.__vertice_fim__ = vertice_fim
        self.__peso__ = peso

    @property
    def id(self):
        return self.__id

    @property
    def vertice_inicio(self):
        return self.__vertice_inicio__
    
    @vertice_inicio.setter
    def vertice_inicio(self,value):
        self.__vertice_inicio__= value

    @property
    def vertice_fim(self):
        return self.__vertice_fim__
    
    @vertice_fim.setter
    def vertice_fim(self,value):
        self.__vertice_fim__= value 

    @property
    def peso(self):
        return self.__peso__
    
    @vertice_inicio.setter
    def vertice_inicio(self,value):
        self.__peso__= value 

    def __eq__(self, other):
        if not isinstance(other, Aresta):
            return False
        
        if(self.id == other.id):
            return True

        return False

    def __str__(self):
        return "Aresta entre o vertice {0} e {1} de peso {2}".format(self.vertice_inicio,self.vertice_fim,self.peso);

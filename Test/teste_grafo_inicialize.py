import sys, os
sys.path.append(os.path.abspath(os.path.join('.', '')))
from GraphModels.Graph.grafo import Grafo
from GraphModels.Graph.vertice import Vertice
from GraphModels.Graph.aresta import Aresta

if __name__ == "__main__":
    vertice_pre_criados = [Vertice("casa"),Vertice("parque"),Vertice("escola"),Vertice("faculdade"),Vertice("empresa")]
    grafo = Grafo(vertice_pre_criados)
    grafo.add_aresta(Aresta(vertice_pre_criados[1],vertice_pre_criados[4]))
    grafo.add_aresta(Aresta(vertice_pre_criados[2],vertice_pre_criados[3]))
    grafo.add_aresta(Aresta(vertice_pre_criados[2],vertice_pre_criados[3]))
    print(grafo)
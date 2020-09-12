import sys, os
sys.path.append(os.path.abspath(os.path.join('.', '')))
from GraphModels.Graph.grafo import Grafo
from GraphModels.Graph.vertice import Vertice
from GraphModels.Graph.aresta import Aresta

if __name__ == "__main__":
    vertices_pre_criados = [Vertice("1",heuristica=200),Vertice("2",heuristica=100),Vertice("3",heuristica=0),
    Vertice("4",heuristica=150),Vertice("5",heuristica=50)]
    grafo = Grafo(vertices_pre_criados)
    grafo.add_aresta(Aresta(Vertice("1"),Vertice("2"),2))
    grafo.add_aresta(Aresta(Vertice("1"),Vertice("4"),4))
    grafo.add_aresta(Aresta(Vertice("2"),Vertice("3"),14))
    grafo.add_aresta(Aresta(Vertice("4"),Vertice("5"),5))
    grafo.add_aresta(Aresta(Vertice("5"),Vertice("3"),2))

    # Teste busca custo uniforme
    print("--------------------------Teste busca custo uniforme--------------------------------")
    print(grafo.buscaCustoUniforme(Vertice("1"),Vertice("3")))

    # Teste busca gulosa
    print("--------------------------Teste busca gulosa--------------------------------")
    print(grafo.buscaGulosa(Vertice("1"),Vertice("3")))

    # Teste busca gulosa
    print("--------------------------Teste busca A*--------------------------------")
    print(grafo.buscaAEstrela(Vertice("1"),Vertice("3")))
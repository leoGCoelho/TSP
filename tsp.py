# Busca por Dijkstra e por Algoritmo Guloso

from collections import deque, namedtuple
import os
import time


inf = float('inf')
aresta = namedtuple('aresta', 'ini, fim, custo') # aresta eh formada por uma dupla contendo o valor da aresta e uma tripla com as ligacoes da aresta e o seu valor

# metodo de construcao da aresta
def make_aresta(ini, fim, custo=1): # aresta eh iniciada com valor 1 representando o infinito
  return aresta(ini, fim, custo)

# classe do grafo
class Grafo:
    # metodo construtor do arranjo da classe
    def __init__(grafo, arestas):
        grafo.arestas = [make_aresta(*aresta) for aresta in arestas]

    # metodo construtor dos vertices
    @property
    def vertices(grafo):
        return set(sum(([aresta.ini, aresta.fim] for aresta in grafo.arestas), []))

    # metodo 'get' dos pares de vertices
    def get_pares(grafo, n1, n2, fins=True):
        if fins:
            parVertices = [[n1, n2], [n2, n1]]
        else:
            parVertices = [[n1, n2]]
        return parVertices

    # metodo de remocao de arestas
    def remove_aresta(grafo, n1, n2, fins=True):
        parVertices = grafo.get_pares(n1, n2, fins)
        arestas = grafo.arestas[:]
        for aresta in arestas:
            if [aresta.ini, aresta.fim] in parVertices:
                grafo.arestas.remove(aresta)

    # metodo de adicao de arestas
    def add_aresta(grafo, n1, n2, custo=1, fins=True):
        parVertices = grafo.get_pares(n1, n2, fins)
        for aresta in grafo.arestas:
            if [aresta.ini, aresta.fim] in parVertices:
                return ValueError('Aresta {} {} ja existe'.format(n1, n2))

        grafo.arestas.append(aresta(ini=n1, fim=n2, custo=custo))
        if fins:
            grafo.arestas.append(aresta(ini=n2, fim=n1, custo=custo))

    # metodo de retorno dos vizinhos do vertice
    @property
    def vizinhos(grafo):
        vizinhos = {vert: set() for vert in grafo.vertices}
        for aresta in grafo.arestas:
            vizinhos[aresta.ini].add((aresta.fim, aresta.custo))

        return vizinhos

    def show(grafo):
        os.system("clear")
        if grafo.arestas == []:
            print('\nGrafo zerado!')
        else:
            for aresta in grafo.arestas:
                print('(' + str(aresta.ini) +', ' + str(aresta.fim) + ', ' + str(aresta.custo) + ')')
        print('\n')



def testDefault():
    return Grafo([])

def test1():
    #ex1.: 6 vertices (abcdef); 9 arestas
    return Grafo([
        ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
        ("b", "d", 14), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
        ("e", "f", 9)])

op = 1 # variavel de opcoes iniciada para while valido

g = Grafo([])
# menu do programa
while True:
    os.system("clear")
    op = input('\n(1) Mostrar Grafo\n(2) Mudar Teste\n(3) Buscar menor caminho\n\n(0) Sair\n\n-> ')
    print('\n')
    os.system("clear")

    # switch menu
    if op == "0":
        break
    else:
        if op == "1":
            g.show()

        else:
            if op == "2":
                opTeste = input('(1) Zerar\n(2) Teste 1\n\n-> ')
                if opTeste == "1":
                    g = testDefault()
                    print('\nGrafo zerado!\n\n')
                else:
                    if opTeste == "2":
                        g = test1()
                        print('\nGrafo de 6 vertices (abcdef) e 9 arestas criado!\n\n')
                    else:
                        print('Comando invalido!\n\n')

            else:
                if op == "3":
                    print(g)

                else:
                    print('Comando invalido!\n')
    time.sleep(3)

os.system("clear")

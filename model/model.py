import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._countries = None
        self._edges = None


    def buildGraph(self,year):
        self.getCountries(year)
        self._graph = nx.Graph()
        self._graph.add_nodes_from(self._countries)
        self._graph.add_edges_from(self._edges)


    def getCountries(self, year):
        (self._countries,self._edges) = DAO.getCountries(year)

    def getReachableState(self,state):
        parziale = []
        parziale.append(state)
        self._reachableCountries = self.ricorsione(parziale)


    def ricorsione(self,parziale):
        count = 0
        for i in parziale:
            for arch in self._graph.edges():
                if arch[0] == i:
                    if arch[1] in parziale:
                        count += 1
                        if count == len(parziale):
                            return parziale

                    else:
                        parziale.append(arch[1])
        self.ricorsione(parziale)

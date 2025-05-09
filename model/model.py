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
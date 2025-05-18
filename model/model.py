import networkx as nx

from database.DAO import DAO

class Model:

    def __init__(self):
        self._countries = None
        self._edges = None


    def buildGraph(self,year):
        self._graph = nx.Graph()
        self._graph.add_nodes_from(DAO.getAllCountries(year))
        self._graph.add_edges_from(DAO.getBorders(int(year)))


    def getReachableState1(self,state):
        tree = nx.bfs_tree(self._graph,state)
        return list(tree.nodes())

    def getReachableState2(self,state):
        tree = nx.dfs_tree(self._graph,state)
        return list(tree.nodes())

    def getReachableState3(self,state):
            visited = []
            self._recursive_visit(state, visited)
            visited.remove(state)
            return visited

    def _recursive_visit(self, state, visited):
            visited.append(state)

            # Iterate through all neighbors of n
            for c in self._graph.neighbors(state):
                # Filter: visit c only if it hasn't been visited yet
                if c not in visited:
                    self._recursive_visit(c, visited)
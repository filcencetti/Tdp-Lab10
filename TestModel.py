from datetime import datetime

from model.country import Country
from model.model import Model

canada = Country("CAN",	20,	"Canada")

mymodel = Model()

mymodel.buildGraph(1980)
start1 = datetime.now()
print("BFS:",len(mymodel.getReachableState1(canada)))
end1 = datetime.now()
print(end1 - start1)
start2 = datetime.now()
print("DFS:",len(mymodel.getReachableState2(canada)))
end2 = datetime.now()
print(end2 - start2)
start3 = datetime.now()
print("Ricorsione:",len(mymodel.getReachableState3(canada)))
end3 = datetime.now()
print(end3 - start3)

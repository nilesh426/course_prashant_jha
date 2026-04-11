class Graph:
    def __init__(self):
        self.adjacency_list={}

    def addvertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex]=[]
            return True
        return False
    
    def addedge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            # self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def PrintGraph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])
    
mygraph=Graph()
mygraph.addvertex('A')
mygraph.addvertex('B')
mygraph.addvertex('C')
mygraph.addvertex('D')
mygraph.addvertex('E')
mygraph.addvertex('F')
mygraph.addedge('A','B')
mygraph.addedge('A','C')
mygraph.addedge('B','A')
mygraph.addedge('B','D')
mygraph.addedge('B','E')
mygraph.addedge('C','A')
mygraph.addedge('C','E')
mygraph.addedge('D','F')
mygraph.addedge('D','E')
mygraph.addedge('D','B')
mygraph.addedge('E','C')
mygraph.addedge('E','B')
mygraph.addedge('E','D')
mygraph.addedge('E','F')
mygraph.addedge('F','D')
mygraph.addedge('F','E')


mygraph.PrintGraph()
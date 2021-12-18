from collections import defaultdict
import random
import datetime 
import time


#This class represents a directed graph using adjacency list representation
class Graph:
    
    # Dictionary to save all distances among all cities
    cc= {'LD' : {'LD':0, 'AD':357, 'VN':1235, 'TR':4400, 'SE':8859},
     'AD' : {'LD':357, 'AD':0, 'VN':936, 'TR':4067, 'SE':8557},
     'VN' : {'LD':1235, 'AD':936, 'VN':0, 'TR':3180, 'SE':8276},
     'TR' : {'LD':4400, 'AD':4067, 'VN':3180, 'TR':0, 'SE':6552},
     'SE' : {'LD':8859, 'AD':8557, 'VN':8276, 'TR':6552, 'SE':0}}

    # Dictionary for default graph
    graph_dict = {'AD':{'LD':357},
            'LD':{'SE':8859},
            'SE':{'TR':6652},
            'TR':{},
            'VN':{'TR':3180,'AD':936}}

# ------ BASIC FUNCTIONS
    
    #constructor
    def __init__(self,vertices):
        self.V= vertices #Number of vertices
        self.graph = defaultdict(list) #default dictionary to store graph
        
    #return graph
    def digraph(self,graph):
        return self.graph

    # function to add an edge to graph
    def add_edge(self,u,v,cost):
            adList = [v,cost]
            self.graph[u].append(adList)
   
    # function to search cost of two vertices
    def search_cost(self,u,v):
        return self.cc[u][v]
    
    # function to add random edges
    def random_edge(self,u,v):
        
        # choose random vertex
        self.u = random.choice(list(self.cc.keys())) #vertex 1
        self.v = random.choice(list(self.cc.keys())) #vertex 2
        
        #if vertex 2 == vertex 1, choose again random vertex
        while (u == v):
            self.v = random.choice(list(self.cc.keys()))
        
        # find cost between two vertex
        cost = self.search_cost(u,v)
        #print(self.cost)
        
        #add new edge between two vertex
        self.add_edge(u,v,cost)
   
    # function to delete edges
    def delete_edge(self,u,v,cost):
        temp = [v,cost]
        if temp in self.graph[u]:
            self.graph[u].remove(temp)
     
# ------ Function 1: Check if the graph is strongly connected by AQILAH SYAHIRAH
    
    #  function to perform DFS
    def DFS(self,v,visited):

        # mark the visited vertex
        visited[v]= True

        #recursive for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFS(i,visited)


    # function that returns reverse graph
    def reverseGraph(self):

        grph = Graph(self.V)

        # recursive for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                grph.add_edge(j,i)
        
        return grph
  
    # function to check the strong connectivity of a graph
    def strongConnect(self): 

        # mark ALL not visited vertex (initialize, first DFS)
        visited =[False]*(self.V)
        
        # perform first DFS from first vertex
        self.DFS(0,visited)

        # return false if first DFS does not visit all vertices
        if any(i == False for i in visited):
            return False

        # create a reversed graph
        g = self.reverseGraph()
        
        # mark ALL not visited vertex (second DFS)
        visited =[False]*(self.V)

        # perform second DFS from first vertex
        # first vertex must be same vertex as the first DFS
        g.DFS(0,visited)

        # return false if second DFS does not visit all vertices
        if any(i == False for i in visited):
            return False

        return True
    
# ------ Function 2: Check if the graph has a cycle by SITI SAKINAH
    
    # function to detect cycle of a graph
    def detectCycle(self, v, visited, rStack):
        
        # mark the current visited vertex and adds to stack
        visited[v] = True
        rStack[v] = True
 
        # do recursive for all vertices 
        # if the nearby vertex is already visited and exist in rStack 
        # then graph is cyclic
        for nearby in self.graph[v]:
            if visited[nearby] == False:
                if self.detectCycle(nearby, visited, rStack) == True:
                    return True
            elif rStack[nearby] == True:
                return True 
 
        # all the vertices have to remove  
        # before ending the recursion stack
        rStack[v] = False
        return False
 
    # return true if graph is cyclic else false
    def detectCycle_bool(self): 
        visited = [False] * (self.V + 1)
        rStack = [False] * (self.V + 1)
        for vertex in range(self.V):
            if visited[vertex] == False:
                if self.detectCycle(vertex,visited,rStack) == True:
                    return True
        return False
        
# ------ Function 3: Select two vertices and compute the shortest path between the vertices by TEOH SIN YEE   
    def dijkstra(self,graph_dict,start,goal): 
        shortest_distance = {}
        predecessor = {}
        unseenNodes = graph_dict
        infinity = 9999999
        path = []
        for node in unseenNodes:
            shortest_distance[node] = infinity
        shortest_distance[start] = 0
     
        while unseenNodes:
            minNode = None
            for node in unseenNodes:
                if minNode is None:
                    minNode = node
                elif shortest_distance[node] < shortest_distance[minNode]:
                    minNode = node
     
            for childNode, weight in graph_dict[minNode].items():
                if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                    shortest_distance[childNode] = weight + shortest_distance[minNode]
                    predecessor[childNode] = minNode
            unseenNodes.pop(minNode)
     
        currentNode = goal
        while currentNode != start:
            try:
                path.insert(0,currentNode)
                currentNode = predecessor[currentNode]
            except KeyError:
                print('Path not reachable')
                break
        path.insert(0,start)
        if shortest_distance[goal] != infinity:
            print("\nRESULT......")
            print('Shortest distance is ' + str(shortest_distance[goal]))
            print('And the path is ' + str(path))
        time.sleep(8)   
    
   
# ----- MAIN FUNCTION
currentDT = datetime.datetime.now()
print ("\n",currentDT.strftime("%a-%Y-%m-%d %H:%M:%S"))

 
while(True):
        
    print("\nGraph Algorithm ")
    print("_______________\n")
    
    g1 = Graph(5) #create 5 edges
    
    #create default graph
    g1.add_edge("LD","SE",8859)
    g1.add_edge("SE","TR",6652)
    g1.add_edge("VN","TR",3180)
    g1.add_edge("VN","AD",936)
    g1.add_edge("AD","LD",357)
    
    #g1.random_edge("VN", "SE")
    
    print ("Auto-generated graph......")
    print("\n")
    
    #print default graph
    print(g1.digraph(g1))

    print("\n1. Check if the graph is strongly connected ")
    print("2. Check if the graph has a cycle")
    print("3. Compute the shortest path between the 2 vertices")
    print("4. Exit");
    choice= int(input (">Enter choice :") )

    if choice==1: # Check if the graph is strongly connected
        print ("The graph is strongly connected") if g1.strongConnect() else print("The graph is not strongly connected")
        time.sleep(8) 

               
    elif choice==2:  # Check if the graph has a cycle
        if g1.detectCycle_bool() == True:
            print ("The graph has a cycle")
        else:
            print ("The graph has no cycle")
        time.sleep(8) 
        
    elif choice==3: #Compute the shortest path between the 2 vertices
        
        print("\nAvailable vertices:")
        print(list(g1.graph_dict.keys()))
        
        v1 = input("Starting vertex: ")
        v2 = input("Ending vertex:")
        
        g1.dijkstra(g1.graph_dict,v1,v2)
       

    elif choice==4: #exit
        break

    else:  
        print("\nInvalid choice. Enter 1-4.")
        
# --- END ----
     
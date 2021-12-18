# Graph-Algorithms-random-city

**Objectives**</br>
The purpose of this assignment is to test your understanding of graph representation and algorithms. You will be required to code the actual algorithms to solve problems that have been discussed in class.
</br></br>
### 1.0 Data Structure and Default Graph (adjacent list)</br>
**Description**</br>
Adjacency List is the data structure that we choose to represent the graphs. An adjacency list is an array A of separate lists. Each element of the array Ai is a list, which contains all the vertices that are adjacent to vertex i. Adjacency list is depend on the type of graphs that we used, for directed graph the edges are order pairs of vertices while undirected graph are unordered pairs. Below, is the default graph for this assignment:</br></br>
![image](https://user-images.githubusercontent.com/69177804/146646628-6bd05ca0-5fd9-44c6-86c8-0129ab0d4a41.png)</br>
<p align="center">Figure 1.1: Default graph</p>

The figure below is the illustration for adjacency list of the default graph. The first line represents the name of the country and second represent weight:</br></br>
<p align="center">
![image](https://user-images.githubusercontent.com/69177804/146647125-f0a4f70d-f2eb-4893-be67-8b21d5bcfbd1.png)
<br>
Figure 1.2: Adjacency list of default graph</p>
</br>

**Justification**</br>
The reason why we choose adjacency list because:

>•	The default graph is considered as sparse graph which means there is a few edges exists and lower memory is used as we are only storing the nodes that exists in the graph compare to adjacency matrix.</br>
•	Based on the time complexity in the Figure below, it shows that most of the adjacency list has less time operation compare to adjacency matrix. </br>
•	It is easier to used adjacency list since the time complexity of graph modification is faster compare to adjacency matrix. It makes the data structure more suitable and efficient for future modification of the graph.</br>
•	In real life problems, mostly uses adjacency list since most of the graphs are dynamic.</br>

<br><br><p align="center">
![image](https://user-images.githubusercontent.com/69177804/146647142-cff9be90-dc66-45f5-a9ed-475057ca6928.png)<br>
Figure 1.3: Time complexity for graphs operation</p>

The only disadvantages of using adjacency list is it require time to list all the nodes that connected to the existing graph O(|V|) in order to find the other node of the edge required but for adjacency matrix, it takes O(1) time to check the distance between two connected nodes as it can just search in the array.</br></br>
### 2.0 Common Graph Functions</br>
<p align="center">
![image](https://user-images.githubusercontent.com/69177804/146647368-2afee350-4921-421a-800f-64c7de57d857.png)
</p>
</br></br>
### 3.0 Strong Connectivity Problem</br>
**Description**</br>
A directed graph (or digraph) is made up of vertices and directed edges, each of which connects an ordered pair of vertices. As a result, reachability is critical in this graph.
A directed graph is strongly connected if it has a path connecting any two pairs of vertices. Connected vertices may travel to any other connected vertices and travel between them by any other connected vertices. To do this, all vertices must be searched, because every vertex is firmly related to all other vertices.	</br></br>
**Justification**</br>
The first way to check that the graph is strongly connected is using checklist for every vertex. Each vertex must reach all other vertices. Next way is using depth first search. DfS is used to find two paths through all the vertices. If no DFS visits all vertices, the graph is not strongly connected.</br></br>
**Flowchart and Explanation**</br><p align="center">
![image](https://user-images.githubusercontent.com/69177804/146647496-7ca9a76e-990e-482d-83c7-94f97aeb0e75.png)</p>
</br>The algorithm above will check if the graph is strongly connected. Firstly, we mark all not visited vertex and then perform DFS from the first vertex. If the DFS not visit all the vertices it will return false and generate random edges until it returns true.</br>
</br>**Results**
<p align="center">
![image](https://user-images.githubusercontent.com/69177804/146647534-a521fa88-4b0e-458e-a3e8-44394781e5fc.png)</p></br>
The diagram above shows the output of the strong connected graph. Since the graph is not strongly connected, so it will generate the random edges until the graph become strongly connected.</br></br>
### 4.0 Cycle Detection Problem
**Description**</br>
In a directed graph, it will consider as a cycle if the vertex is visited second time. It can be determined by marking the visited vertices. The route only can be used once so it will use another route until it reaches the already visited vertex. The problem can be solved by using Depth First Search algorithm. The application of a cycle detection including cryptographic hash function, money laundering and detection of deadlocks.
</br></br>
**Justification**</br>
A cycle of a directed graph can be check by using Depth First Search Algorithm. The algorithm will visit all the vertices available and if the vertex already visited it, the algorithm will detect that the graph contains a cycle.  If all the vertices visited but it did not reach any vertices for a second time, the graph is considered as acyclic. 
</br></br>
**Flowchart and Explanation**</br>





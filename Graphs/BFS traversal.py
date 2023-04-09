'''Given an undirected and disconnected graph G(V, E), print its BFS traversal.

Note:
1. Here you need to consider that you need to print BFS path starting from vertex 0 only. 
2. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
3. E is the number of edges present in graph G.
4. Take graph input in the adjacency matrix.
5. Handle for Disconnected Graphs as well

Input Format :
The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains space separated two integers, that denote that there exists an edge between vertex a and b.

Output Format :
Print the BFS Traversal, as described in the task.

Constraints :
0 <= V <= 1000
0 <= E <= (V * (V - 1)) / 2
0 <= a <= V - 1
0 <= b <= V - 1
Time Limit: 1 second

Sample Input 1:
4 4
0 1
0 3
1 2
2 3

Sample Output 1:
0 1 3 2'''

import queue

#using adjacency matrix
class Graph():
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)] for j in range(nVertices)]

    #breadth first search
    def __bfsHelper(self,sv,visited):
        q=queue.Queue()
        q.put(sv)
        visited[sv]=True
        count=0
        while not q.empty():
            curr_vertice=q.get()
            print(curr_vertice,end=' ')
            for i in range(self.nVertices):
                if self.adjMatrix[curr_vertice][i]>0 and visited[i]==False:
                    q.put(i)
                    visited[i]=True

    def bfs(self):
        visited=[False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i]==False:
                self.__bfsHelper(i,visited)


    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1

    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0

    def containsEdge(self,v1,v2):
        if self.adjMatrix[v1][v2]>0:
            return True
        else:
            return False
          
    def __str__(self):
        return str(self.adjMatrix)



V_E=(input().split())
vertices=int(V_E[0])
edges=int(V_E[1])
g=Graph(vertices)
for i in range(edges):
    v1_v2=(input().split())
    v1=int(v1_v2[0])
    v2=int(v1_v2[1])
    g.addEdge(v1,v2)
g.bfs()

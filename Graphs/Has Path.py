'''Given an undirected graph G(V, E) and two vertices v1 and v2 (as integers), check if there exists any path between them or not. 
Print true if the path exists and false otherwise.

Note:
1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
2. E is the number of edges present in graph G.

Input Format :

The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains two integers, that denote that there exists an edge between vertex 'a' and 'b'.
The following line contain two integers, that denote the value of v1 and v2.

Output Format :

The first and only line of output contains true, if there is a path between v1 and v2 and false otherwise.

Constraints :

0 <= V <= 1000
0 <= E <= 1000
0 <= a <= V - 1
0 <= b <= V - 1
0 <= v1 <= V - 1
0 <= v2 <= V - 1
Time Limit: 1 second

Sample Input 1 :
4 4
0 1
0 3
1 2
2 3
1 3

Sample Output 1 :
true

Sample Input 2 :
6 3
5 3
0 1
3 4
0 3

Sample Output 2 :
false'''

#using adjacency matrix
#Depth First Search 
class Graph():
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1

    def __hasPathHelper(self,v1,v2,visited):
        if self.containsEdge(v1,v2):
            return True
        for i in range(self.nVertices):
            if self.adjMatrix[v1][i]>0 and visited[i]==False:
                visited[i]=True
                temp_ans=self.__hasPathHelper(i,v2,visited)
                if temp_ans==True:
                    return True
        return False


    def hasPath(self,v1,v2):
        visited=[False for i in range(self.nVertices)]
        ans=self.__hasPathHelper(v1,v2,visited)
        return ans

    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0

    def containsEdge(self,v1,v2):
        if self.adjMatrix[v1][v2]>0 or self.adjMatrix[v2][v1]>0:
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
has_path_vertices=(input().split())
v1=int(has_path_vertices[0])
v2=int(has_path_vertices[1])
if v1<vertices and v2<vertices:
    ans=g.hasPath(v1,v2)
else:
    ans=False
if ans==True:
    print('true')
else:
    print('false')


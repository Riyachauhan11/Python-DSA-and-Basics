'''Given an undirected graph G(V, E) and two vertices v1 and v2 (as integers), 
find and print the path from v1 to v2 (if exists). 
Print nothing if there is no path between v1 and v2.

Find the path using BFS and print the shortest path available.

Note:

1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
2. E is the number of edges present in graph G.
3. Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
4. Save the input graph in Adjacency Matrix.

Input Format :

The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains two integers, that denote that there exists an edge between vertex a and b.
The following line contain two integers, that denote the value of v1 and v2.

Output Format :

Print the path from v1 to v2 in reverse order.

Constraints :

2 <= V <= 1000
1 <= E <= (V * (V - 1)) / 2
0 <= a <= V - 1
0 <= b <= V - 1
0 <= v1 <= 2^31 - 1
0 <= v2 <= 2^31 - 1
Time Limit: 1 second

Sample Input 1 :

4 4
0 1
0 3
1 2
2 3
1 3

Sample Output 1 :

3 0 1'''
import queue
# Write your code here
class Graph():
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1


    def __getPathHelper(self,sv,ev,visited,parent_dict):

        q=queue.Queue()
        q.put(sv)

        visited[sv]=True

        while not q.empty():
            curr_vertice=q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[curr_vertice][i]>0 and visited[i]==False:
                    q.put(i)
                    visited[i]=True
                    parent_dict[i]=curr_vertice
                if i==ev:
                    break
        return parent_dict
        

    def getPath(self,sv,ev):
        visited=[False for i in range(self.nVertices)]
        parent_dict={}
        final_dict= self.__getPathHelper(sv,ev,visited,parent_dict)
        main_ans=[]
        no=ev
        if no not in final_dict:
            return None
        while no!=sv:
            main_ans.append(no)
            no=final_dict[no]
        main_ans.append(sv)
        return main_ans


    

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
get_path_vertices=(input().split())
v1=int(get_path_vertices[0])
v2=int(get_path_vertices[1])
path=g.getPath(v1,v2)
if path!=None:
    for i in path:
        print(i,end=' ')
else:
    print()

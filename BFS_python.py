#!/usr/bin/env python
# coding: utf-8

# In[4]:


from collections import defaultdict

# Directed graph with adjacency list
class Graph:
    def __init__(self):
        
        #Dictionary to store graph
        self.graph = defaultdict(list)
        
    #Function to add an edge to graph
    def add_edge(self,u,v):
        self.graph[u].append(v)
        
    #Function to print BFS from a graph
    def BFS(self, s):
        #Mark all vertices as not visited
        visited = [False]*(len(self.graph))
        
        #Create a queue for BFS
        queue = []
        
        #Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
        
        while queue:
            #Dequeue a vertex from queue and print it
            s = queue.pop()
            print (s, end = " ")
            
            #Get all adjacent vertices of the dequeued vertex s.
            #If adjacent has not been visited, then mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    
            
#Driver Code
#Create a graph
g = Graph()

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,3)

print("BFS")
g.BFS(2)

  


# In[ ]:





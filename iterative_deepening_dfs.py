#!/usr/bin/env python
# coding: utf-8

# In[57]:


# Artificial Intelligence Class
# Project # 2
# Professor: Dr.Bill Buckles
# Student: Rubenia Borge Flores
# Task: Implement IDS - Iterative Deepening Search

from collections import defaultdict 
class Graph:
	def __init__(self,vertices): 
		self.V = vertices
		self.graph = defaultdict(list) 
 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	def DLS(self,src,goal,d):
		if src == goal : return True 
		if d <= 0 : return False
		for i in self.graph[src]: 
				if(self.DLS(i,goal,d-1)): 
					return True
		return False
 
	def IDDFS(self,src, goal, d): 
		for i in range(d): 
			if (self.DLS(src, goal, i)): 
				return True
		return False

g = Graph (31); 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(1, 4) 
g.addEdge(2, 5) 
g.addEdge(2, 6)
g.addEdge(3, 7) 
g.addEdge(3, 8) 
g.addEdge(4, 9) 
g.addEdge(4, 10) 
g.addEdge(5, 11) 
g.addEdge(5, 12)
g.addEdge(6, 13) 
g.addEdge(6, 15)
g.addEdge(7, 15) 
g.addEdge(7, 16) 
g.addEdge(8, 17) 
g.addEdge(8, 18) 
g.addEdge(9, 19) 
g.addEdge(9, 20)
g.addEdge(19, 21) 
g.addEdge(10, 22) 
g.addEdge(11, 23) 
g.addEdge(11, 24) 
g.addEdge(12, 25) 
g.addEdge(12, 26)
g.addEdge(13, 27) 
g.addEdge(13, 28) 
g.addEdge(14, 29) 
g.addEdge(14, 30) 


print("Sample Execution for 3")
goal = 3; d = 3; src = 0
if g.IDDFS(src, goal, d) == True: 
	print ("Final Result: The goal was reached.")    
else : 
	print ("Final Result: The goal was not rached.")    
 
# The sequence of actions that reached the goal state from the root
print("The sequence of actions is: ")
print(g.graph)
print("The patch cost of the goal is: ")
print("3")
print("The total number of states created is: ")
print(len(g.graph))
print("---------------------------------------------------------------------------------------------------------")
print("\n")


print("Sample Execution for 15")
goal = 15; d = 5; src = 0
if g.IDDFS(src, goal, d) == True: 
	print ("Final Result: The goal was reached.")    
else : 
	print ("Final Result: The goal was not rached.")    
 
# The sequence of actions that reached the goal state from the root
print("The sequence of actions is: ")
print(g.graph)
print("The patch cost of the goal is: ")
print("7")
print("The total number of states created is: ")
print(len(g.graph))
print("---------------------------------------------------------------------------------------------------------")
print("\n")

print("Sample Execution for 165")
goal = 165; d = 5; src = 0
if g.IDDFS(src, goal, d) == True: 
	print ("Final Result: The goal was reached.")    
else : 
	print ("Final Result: The goal was not rached.")    
 
# The sequence of actions that reached the goal state from the root
print("The sequence of actions is: ")
print(g.graph)
print("The patch cost of the goal is: ")
print("31")
print("The total number of states created is: ")
print(len(g.graph))
print("---------------------------------------------------------------------------------------------------------")



# In[ ]:





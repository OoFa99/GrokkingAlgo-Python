from collections import defaultdict
import queue

class Graph:
    vertices_num = 0
    adjecency_lists = defaultdict(list)
    
    def __init__(self, vert_num):
        self.vertices_num = vert_num
        
    def add_edge(self, v1, v2):
        self.adjecency_lists[v1].append(v2)
        
    def BFS(self, start, value):
        visited = [False] * (len(self.adjecency_lists))
        queue = []
        
        queue.append(start)
        visited[start] = True
        
        while queue:
            start = queue[0]
            if start == value: 
                return start
            else: 
                queue.pop()
                print(start, end = " ")
            
            for i in self.adjecency_lists[start]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        

v1, v2, counter = 0, 0, 1
 
vertices_num = int(input("This is the BFS algorithm practice \nPlease enter the number of vertices in the graph : "))
g = Graph(vertices_num)
 
start = int(input("\nPlease enter the value of the root node : "))
 
print("\nPlease enter the directed edges of the graph :- \n")
while(True):
    v1, v2 = tuple(map(int, input("Enter the edge number {} : ".format(counter)).split()))
    
    if((v1 >= vertices_num) or (v2 >= vertices_num)):
        print("\nExceeded the number of vertices entered.\n")
        break
    g.add_edge(v1, v2)
    counter += 1

value = int(input("\n\n Enter the value you want to search for : "))

print("The value : {} exists in the graph".format(g.BFS(start, value)))
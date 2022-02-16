
v1, v2, counter = 0, 0, 1
 
vertices_num = int(input("This is the BFS algorithm practice \nPlease enter the number of vertices in the graph : "))
# Define the graph object
 
start = int(input("\nPlease enter the value of the root node : "))
 
print("\nPlease enter the directed edges of the graph :- \n")
while(True):
    v1, v2 = input("Enter the edge number {}".format(counter) + " : ")
    if((v1 >= vertices_num) or (v2 >= vertices_num)):
        print("\nExceeded the number of vertices entered.\n")
        break
    #g.add edge(v1, v2)
    counter += 1

value = int(input("\n\n Enter the value you want to search for : "))

print("The value : {} exists in the graph".format(g.BFS(start, value)))
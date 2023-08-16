#Kalyan Venkat Madireddy
#801306030

import sys
import numpy as np
class BinaryHeap:
    """
            This class, BinaryHeap, is a binary min-heap data structure implementation.

        __init__(self) creates an empty heap by initializing it with a list containing a single entry (0, None).
        heappush(self, heap, element) creates a new element in the heap while preserving the heap property.

        heappop(self, heap) removes the heap's root element while keeping the heap property.
        perc_up(self, i, heap) raises a newly inserted element in the heap till the heap property is preserved.
        perc_down(self, i, heap) pushes a heap element down until the heap property is maintained.
        min_child(self, i, heap) yields the index of the node's smallest child.
    """
    def __init__(self):
        self.heap_list = [(0, None)]
        self.current_size = 0
    def heappush(self, heap, element):
        heap.append(element)
        self.current_size += 1
        self.perc_up(self.current_size, heap)
    def heappop(self, heap):
        if self.current_size == 0:
            return None
        root_val = heap[1]
        heap[1] = heap[self.current_size]
        self.current_size -= 1
        heap.pop()
        self.perc_down(1, heap)
        return root_val
    def perc_up(self, i, heap):
        while i // 2 > 0:
            if heap[i][0] < heap[i // 2][0]:
                tmp = heap[i // 2]
                heap[i // 2] = heap[i]
                heap[i] = tmp
            i //= 2

    def perc_down(self, i, heap):
        while i * 2 <= self.current_size:
            mc = self.min_child(i, heap)
            if heap[i][0] > heap[mc][0]:
                tmp = heap[i]
                heap[i] = heap[mc]
                heap[mc] = tmp
            i = mc
    def min_child(self, i, heap):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if heap[i * 2][0] < heap[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

class Vertex:
    """
        A node in a graph is represented by the Class Vertex.

    __init__(self, name): Creates a Vertex object with a name, an empty adjacency_list, and a boolean flag indicating whether the node is marked down.
    add_edge(self, vertex, weight): Adds an edge with the supplied vertex and weight to the node's adjacency_list and adjacency_list_copy.
    mark_down(self): Sets the is_down flag to True to indicate that the node is down.
    mark_up(self): Sets the is_down flag to False to mark the node as up.

    """
    def __init__(self, name):
        self.name = name
        self.adjacency_list = {}
        self.adjacency_list_copy = {}
        self.is_down = False
    def add_edge(self, vertex, weight):
        self.adjacency_list[vertex] = weight
        self.adjacency_list_copy[vertex] = weight
    def mark_down(self):
        self.is_down = True
    def mark_up(self):
        self.is_down = False

class Graph:
    """
        A graph representing a graph data structure. It offers methods for adding vertices and edges to the graph, deleting edges, marking vertices as up or down, and utilizing Dijkstra's algorithm to calculate the shortest path between two vertices. It also has methods for printing the graph and getting all accessible vertices from a particular vertex.


    The following methods are available in the Graph class:

    __init__(self): Creates an empty dictionary to contain the vertices in the Graph object.
    add_vertex(self, vertex): Inserts a new vertex into the dictionary of vertices to add a new vertex to the graph.
    get_vertex(self, name): If the vertex with the supplied name exists in the graph, it is returned.
    add_edge(self, v1, v2, weight): Creates a new edge in the graph between two vertices. If If the vertices do not already exist in the graph, they are added first.
    delete_edge(self, v1, v2): Removes an edge in the graph between two vertices.
    edgedown(self, v1, v2): Sets the weight of an edge between two vertices to infinity.
    edgeup(self, v1, v2): Returns the original weight of an edge between two vertices.
    vertexdown(self, name): Indicates that a vertex is down.
    vertexup(self, name): Indicates that a vertex is up.
    build_graph(self, network_file): Creates a graph by reading vertex and edge data from a file.
    __str__(self): A string representation of the graph is returned.
    dijkstra(self, start_vertex, end_vertex): Dijkstra's algorithm is used to find the shortest path between two vertices in a network.
    print_graph(self): This function prints the graph.
    get_reachable_vertices(self): Returns all reachable vertices in the graph from a specified vertex.

    """
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        self.vertices[vertex.name] = vertex
    def get_vertex(self, name):
        return self.vertices.get(name)
    def add_edge(self, v1, v2, weight):
        if v1 not in self.vertices:
            self.add_vertex(Vertex(v1))
        if v2 not in self.vertices:
            self.add_vertex(Vertex(v2))
        if v2 in self.vertices[v1].adjacency_list:
            self.vertices[v1].adjacency_list[v2] = weight
            self.vertices[v1].adjacency_list_copy[v2] = weight
        else:
            self.vertices[v1].add_edge(v2, weight)
    
    def delete_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            if v2 in self.vertices[v1].adjacency_list:
                del self.vertices[v1].adjacency_list[v2]
                del self.vertices[v1].adjacency_list_copy[v2]
    
    def edgedown(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            if v2 in self.vertices[v1].adjacency_list:
                original_val=self.vertices[v1].adjacency_list[v2]
                self.vertices[v1].adjacency_list[v2] = np.inf
    def edgeup(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            if v2 in self.vertices[v1].adjacency_list:
                self.vertices[v1].adjacency_list[v2] = self.vertices[v1].adjacency_list_copy[v2]

    def vertexdown(self, name):
        vertex = self.get_vertex(name)
        if vertex:
            vertex.mark_down()
        else:
            print("Vertex not found in graph")

    def vertexup(self, name):
        vertex = self.get_vertex(name)
        if vertex:
            vertex.mark_up()
        else:
            print("Vertex not found in graph")
    def build_graph(self, network_file):
        with open(network_file, "r") as f:
            for line in f:
                v1, v2, weight = line.strip().split()
                self.add_edge(v1, v2, weight)
                self.add_edge(v2, v1, weight)
    def __str__(self):
        result = []
        for vertex in self.vertices.values():
            result.append(f"{vertex.name}:")
            for adj_vertex, weight in vertex.adjacency_list.items():
                result.append(f"    {adj_vertex} {weight:}")
        return "\n".join(result)
    

    def dijkstra(self, start_vertex, end_vertex):
        """
            Dijkstra's technique is used to discover the shortest path in a weighted network.

        Args: - graph: a dictionary containing nodes as keys and a collection of tuples (neighbor, edge weight) as values.
        - start: the pathfinding algorithm's beginning node.

        Distances: a dictionary with nodes as keys and the shortest distance between them and the beginning node as values.
        - paths: a dictionary containing nodes as keys and a list of nodes according to their shortest path from the beginning node.

      """

  
        heaper=BinaryHeap()
        distances = {}  # Distances to all vertices
        previous = {}  # Previous vertex in the path
        visited = set()  # Visited vertices
        
        # Initialize distances
        for vertex in self.vertices:
            if vertex == start_vertex:
                distances[vertex] = 0
                heaper.heappush(heaper.heap_list, (0, vertex))
            else:
                distances[vertex] = np.inf
            
            previous[vertex] = None
        
        while heaper:
            (distance, current_vertex) = heaper.heappop(heaper.heap_list)
            
            if current_vertex == end_vertex:
                break
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            
            for neighbor, weight in self.vertices[current_vertex].adjacency_list.items():
                if self.vertices[neighbor].is_down:
                    continue
                tentative_distance = distance + float(weight)
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    previous[neighbor] = current_vertex
                    heaper.heappush(heaper.heap_list,(tentative_distance, neighbor))
        
        path = []
        current_vertex = end_vertex
        while current_vertex != start_vertex:
            if current_vertex is None:
                return None
            path.insert(0, current_vertex)
            current_vertex = previous[current_vertex]
        
        path.insert(0, start_vertex)
        total_time =np.round(distances[end_vertex],2)
        return path, total_time
    
    def print_graph(self):
        result = []
        for vertex_name in sorted(self.vertices):
            vertex = self.vertices[vertex_name]
            if vertex.is_down== True:
                aab=vertex.name+" "+"DOWN"
                result.append(f"{aab}")
            else:
                result.append(f"{vertex.name}")
            for adj_vertex, weight in sorted(vertex.adjacency_list.items()):
                if weight==np.inf:
                   weight= vertex.adjacency_list_copy[adj_vertex]
                   aac= (f"    {adj_vertex} {weight}")
                   result.append(aac+" "+"DOWN")
                else:
                    result.append(f"    {adj_vertex} {weight}")
        return "\n".join(result)
    


    def get_reachable_vertices(self):
        """"
        This method returns a dictionary of a graph's accessible vertices. There is no need for debate. The function begins by creating an empty dictionary and an empty list. It then runs across the graph, sorting each vertex by name. It examines each vertex to see whether it is not down. If the vertex is not down, a depth-first search is performed to discover all accessible vertices from that vertex. The function then adds a key-value pair to the accessible dictionary, where the key is the vertex name and the value is a sorted list of reachable vertex names. Finally, the method returns the dictionary that can be accessed.

        """
        # This algorithm implements a DFS to find the reachable nodes hence the time complexity of this would be 
        #equal to O(V+E) and for v vertices, it's equal to O(V(V+E)). 
        reachable = {}
        result=[]
        for vertex_name in sorted(self.vertices):
            vertex = self.vertices[vertex_name]
            if vertex.is_down  == False:
                stack = [vertex]
                visited = set()
                while stack:
                    current = stack.pop()
                    if current.is_down==False:
                        visited.add(current)
                    for neighbor in current.adjacency_list:
                        if self.vertices[neighbor] != np.inf and self.vertices[neighbor] not in visited:
                            stack.append(self.vertices[neighbor])
                reachable[vertex.name] = sorted([v.name for v in visited])
        return reachable
        

def main():
    g = Graph()
    input_graph_file = sys.argv[1]
    input_queries_file = sys.argv[2]
    output_file = sys.argv[3]

    # building graph 
    g.build_graph(input_graph_file)
    Out_put_file_list=list()


    with open(input_queries_file) as f:
        lines = f.readlines()
        print("Note: I'm printing the O/P to the console and also gnerating the Outputfile witht the answers to queries as output.txt ")
    for line in lines:
        query=line
        if query.startswith("addedge"):
            _, tail, head, time = query.split()
            g.add_edge(tail, head, time)
        if query.startswith("deleteedge"):
            _, tail, head = query.split()
            g.delete_edge(tail, head)
        if query.startswith("edgedown"):
            _, tail, head = query.split()
            g.edgedown(tail, head)
        if query.startswith("edgeup"):
            _, tail, head = query.split()
            g.edgeup(tail, head)
        if query.startswith("vertexdown"):
            _, tail = query.split()
            g.vertexdown(tail)
        if query.startswith("vertexup"):
            _, tail = query.split()
            g.vertexup(tail)
        if query.startswith("path"):
            _, tail, head= query.split()
            path,weigt_took=g.dijkstra(tail, head)
            out_str=""
            for each in path: 
                out_str=out_str+" "+str(each)
            xyz=out_str + " "+str(weigt_took)
            print(xyz)
            Out_put_file_list.append(xyz)
            Out_put_file_list.append(" ")
            print()
        if query.startswith("print"):
            atoz=g.print_graph()
            print(atoz)
            print()
            Out_put_file_list.append(atoz)
            Out_put_file_list.append(" ")
        if query.startswith("reachable"):
            reachable=g.get_reachable_vertices()
            for each_vertex in reachable:
                print(each_vertex)
                Out_put_file_list.append(each_vertex)
                for leng in range(len(reachable[each_vertex])):
                    if(each_vertex!=reachable[each_vertex][leng]):
                        print("  "+reachable[each_vertex][leng])
                        Out_put_file_list.append("  "+reachable[each_vertex][leng])
            print()
            Out_put_file_list.append(" ")
        if query.startswith("quit"):
            break
    
    print()
    print()
   
    #writing to the output file
    with open("output.txt", "w") as f:
        original_stdout = sys.stdout
        sys.stdout = f
        for each_line in Out_put_file_list:
            print(each_line)
        sys.stdout = sys.__stdout__



    print()
    print()
    print("Now done with printing to console and to the output file")
    print("Now, to test new queries on the the graph press 1 continue or else press any other number...")
    k=int(input("Enter your choice..."))
    if(k==1):
        while True:
            query = input("Enter your Query, quit command gets you out of loop...")
            if query.startswith("addedge"):
                _, tail, head, time = query.split()
                g.add_edge(tail, head, time)
            if query.startswith("deleteedge"):
                _, tail, head = query.split()
                g.delete_edge(tail, head)
            if query.startswith("edgedown"):
                _, tail, head = query.split()
                g.edgedown(tail, head)
            if query.startswith("edgeup"):
                _, tail, head = query.split()
                g.edgeup(tail, head)
            if query.startswith("vertexdown"):
                _, tail = query.split()
                g.vertexdown(tail)
            if query.startswith("vertexup"):
                _, tail = query.split()
                g.vertexup(tail)
            if query.startswith("path"):
                _, tail, head= query.split()
                path,weigt_took=g.dijkstra(tail, head)
                out_str=""
                for each in path: 
                    out_str=out_str+" "+str(each)
                print(out_str + " "+str(weigt_took))
            if query.startswith("print"):
                atoz=g.print_graph()
                print(atoz)
            if query.startswith("reachable"):
                reachable=g.get_reachable_vertices()
                for each_vertex in reachable:
                    print(each_vertex)
                    for leng in range(len(reachable[each_vertex])):
                        if(each_vertex!=reachable[each_vertex][leng]):
                            print("  "+reachable[each_vertex][leng])
            if query.startswith("quit"):
                break
    
    print("Thank you")

    


if __name__=="__main__":
    main()

    




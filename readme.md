
Project Brief/Introduction: 

The project entails creating and maintaining a data communication network that routes data packets using Dijkstra's shortest path method, which is based on the criterion of reducing the total time required for data to reach its destination. The network is made up of routers that are linked together via physical cables or links that can fail due to cable cutting or router breakdowns. Furthermore, links may be dynamically added or withdrawn.
To begin the project, a graph representing the network's starting state is constructed using an input file supplied through the command line. The input file structure is straightforward, with each connection represented by two directed edges defined by the names of its two vertices and the transmission time. The transmission timings are simply floating point values, while the vertices are simply strings with no spaces. Two directed edges are added to the graph for each input connection, one in each direction.
The software then reads standard input queries to update the graph, identify the shortest path between any two vertices, output the graph, and locate accessible groupings of vertices. Adding or removing directed edges, labeling directed edges or vertices as "down" or "up," and designating vertices as "down" are all input queries for updating the graph.
When a directed edge is added or its transmission time is altered, the graph is updated by adding a single directed edge in the given direction. If the edge is already present on the graph, its transmission time is adjusted. If a vertex does not already exist in the graph, it is added.
When a directed edge is deleted, it removes the given edge from the graph but does not remove the vertices. Nothing is done if the edge does not exist.
When a directed edge is designated as "down," it is marked as unusable, while its counterpart directed edge in the other direction is unaffected. When a directed edge is indicated as "up," it indicates that it is ready for usage, and its prior transmission time is utilized.
None of a vertices's edges may be utilized when it is marked as "down," however designating a vertex as "down" does not cause any of its incoming or outgoing edges to be marked as "down." The graph can include "up" edges that enter and exit a "down" vertex.
The software utilizes Dijkstra's shortest path method with the objective of reducing the total time needed for data to reach the destination to discover the shortest path between any two vertices in the graph depending on its current state. The shortest time path is determined by minimizing the sum of the transmission times of the connections in the path. The software computes the optimum path based on the data accessible to each router, which normally includes a comprehensive representation of the network.
The software simply produces the current state of the graph, including all vertices and directed edges, as well as their transmission timings and availability status, to print the graph.
Finally, the software can identify reachable sets of vertices, which are vertices that can be reached from a particular beginning vertex. This is accomplished by traversing the graph from the beginning vertex and marking visited vertices as "seen" using a depth-first search technique. The software returns the set of vertices that may be reached from each beginning vertex in the graph.
Finally, the project entails the creation and maintenance of a data communication network that routes data packets using Dijkstra's shortest path method. The network is made up of routers connected by physical cables or links, which might fail due to cable cuts or router breakdowns, and links can be dynamically added or withdrawn. To update the graph, identify the shortest path between any two vertices, print the graph, and locate reachable sets of vertices, the software reads input queries from standard input.
***********************************************************************************************************************************************************************

This submission contains 2 files including this in total.
1. The code file named as "programming_assignment2_Graphs.py"
2. This File that is Readme File 

# How to run this is given at the bottom.

***********************************************************************************************************************************************************************

Implementation: [Structural overview]

1. The vertices are initialized using the vertex class and add edge function adds the edge between the two edges and assigns the weight to them. Note: The edges that are created at the begining of the graph creation are double headed, which means A<->B . 
2. Then we have this, graph class, which does almost everything. It contains so many functions.
	i. The function add_edge adds the directed edge from vertex v1 to vertex v2 and assigns some weight.
	ii. The function delete_edge deleted the existing edge if it exists.
	iii. The function edge_down turns the edge as down which is like shutting down the edge without actually deleting it, because it can later be retrieved if we want.
	iv. The function edge_up to do the opposite of iii.
	v. The function vertex down for shutting down the vertex literally not allowing anything through it.
	vi. The function vertex up to reverse the effect of v.
	vii. The Dijkshtras algorithm for finding the shortest path between the two nodes using min heap.
	viii. The Print function to print in alphabetical order the graph.
	ix. The reachable function that uses the dfs approach to find the nodes that are reachable from each vertex and prints them.
3. We also defined the heap class for writing the functions like heap insertion and heap pop which we used in our dijkshtras algorithm.
4. We also wrote the function quit to exit when ever we want.

That's what happening on a bief, the algorithmic pseudocode for the djkshtras and the reachable vertices is written below

***********************************************************************************************************************************************************************

Algorithms/Pseudocode:

ALgorithm Dijkshtra's	

1. Set up a min heap Q, distances, and a visited set.
2. Set the initial vertex's distance to 0 and all other vertices' distances to infinity.
3. Insert the first vertex into the priority queue.
4. As long as the priority queue is not empty:
	a. From the priority queue, dequeue the vertex with the shortest distance.
	b. If the dequeued vertex is the end vertex, the process is terminated and the shortest path and distance are returned.
	c. If the dequeued vertex has already been visited, skip it and proceed.
	d. Otherwise, mark the dequeued vertex as visited and update the distances between it and its neighbors.
	e. For each dequeued vertex's neighbour vertex:
		i. Skip the nearby vertex and proceed if it has already been visited.
		ii. Add the distance of the dequeued vertex and the weight of the edge connecting them to calculate the tentative distance to the neighboring vertex.
		iii. Update the distance and enqueue the nearby vertex with its updated distance if the tentative distance is smaller than the previously computed distance.
5. Return None if the final vertex is not accessible from the originating vertex.

o/p: The ultimate result will be the shortest path and distance between the beginning and ending vertices.

## The time complexity of Dijkstra's algorithm using a binary heap for priority queue implementation is O((E+V)logV), where E is the number of edges and V is the number of vertices in the graph.

...................................................................

Algorithm Reachable

1. Create an empty dictionary named "reachable".
2. Create a new empty list called "result".
3. In sorted order, for each vertex in the graph:
    a. If the vertex is not down, perform the following actions:
        i. Create a stack using the current vertex as the first element.
        ii. Create a new empty set called "visited".
        iii. As long as the stack is not empty:
            1. Select the top vertex from the stack and add it to the visited list.
            2. For each current vertex's neighbor:
                a. If the neighbor is still up and hasn't been visited, add it to the stack.
        iv. Insert the sorted list of visited vertex names into the accessible dictionary as the key, with the current vertex's name as the value.
4. Return the dictionary that can be reached.

## The time complexity of this algorithm is O(V*(V+E)), where V is the number of vertices and E is the number of edges in the graph




***********************************************************************************************************************************************************************

How to run these programs ?

1. Open the command prompt or cmd on windows.
2. Navigate to the Directory where the code is Saved. Example if the code is in D directory use "D:" to change the directories.
3. Then set the current location using cd "file path " to go to the exact file location where the .py program file is present.
4. Then to run the executable file type: python programming_assignment2_Graphs.py <inputFileName.txt> <queryies_file.txt> <O/P file.txt>
	Example: command: python programming_assignment2_Graphs.py network.txt queries.txt output.txt
	Result:  # The output for the queries which prints is printed on to the console and also the output is stored in the output file .
	         Apart from this, after executing this, the program asks you if you want to check any other commands just by typing them, if you press 1
	         you will be looped to enter command after command untill u type the quit command.

***********************************************************************************************************************************************************************

Data Structures Used:

Graph: A graph data structure that provides methods for adding and removing vertices and edges, marking vertices as up or down, and calculating the shortest path between two vertices using Dijkstra's algorithm.

Min heap: Data structure for implementing the Dijkstra's algorithm.

Dictionary: Data structure used to store the edges of the graph along with the weights. it's the basis for the graph.

List: The data structure used in many places in the code, especially in the priting and storing the output before printing out to the console or before writing it into the .txt file. 



***********************************************************************************************************************************************************************
 What works and what not works:

works: 
1. This algorithm needs the input file, query file and even if you forget to add some commands in to your queries file or if u want to check only one command or so, you can just do it using the test  more commands option at the end of the execution.
2. Works well for finding the shortest path, with the binary heap which is also impleemnted using the seperate class with functions.
3. works well when the last line in the input file or even in the looped command interface at the end is quit command.
4. Or else it stucks in the loop .
5. Tested only on my laptop which is windows 11, not tested on macbook, ubuntu etc.



***********************************************************************************************************************************************************************

Specifications:
Programming Language: Python 
Version: Python 3.11.2

***********************************************************************************************************************************************************************


	         







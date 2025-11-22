Project Statement: BFS Shortest Path Finder

🎯 Problem Statement


The core problem addressed is the need for an efficient and visually understandable solution to find the shortest path between a designated starting point (S) and a goal state (G) within a two-dimensional, unweighted grid environment (a maze). While many search algorithms can find a path, the requirement is specifically for a method that guarantees optimality (the shortest path in terms of steps) and allows for step-by-step visualization of the search process for educational purposes.


🧭 Scope of the Project


The scope of this project is focused and highly defined:

1.	Environment: The application operates within a terminal environment using Python's curses library for rendering.
2.	Data Structure: The maze is a static, predefined 2D list (array) of characters.
3.	Algorithm: The exclusive pathfinding technique used is Breadth-First Search (BFS), which ensures the calculated path is the shortest possible route.
4.	Functionality: The primary function is to:
o	Locate the 'S' and 'G' nodes.
o	Execute the BFS search, visualizing the expansion of the search frontier.
o	Upon reaching the goal, display the final shortest path.
5.	Exclusions: The project does not include:
o	Support for weighted graphs (Dijkstra's or A* algorithms).
o	Maze generation functionality (the maze is hardcoded).
o	Graphical User Interface (GUI) or web interface.
o	Multi-user functionality or persistent storage.
👥 Target Users
The primary target audience for this project is highly focused on learning and demonstration:
•	Computer Science Students: Individuals studying graph theory, search algorithms, and data structures who need a clear, working example of BFS.
•	Educators/Instructors: People who require a simple, visual tool to demonstrate the mechanics and optimality guarantee of the BFS algorithm in a controlled environment.
•	Developers: Those looking for a concise, practical implementation of BFS in Python as a reference or learning resource.
 

✨ High-Level Features

Guarantees the path found between 'S' and 'G' is the minimum number of steps.

Provides a clear, non-distracting interface suitable for algorithm demonstration.

Allows users to observe the level-by-level exploration behavior inherent to BFS.

Ensures robust and safe traversal within the defined grid limits.
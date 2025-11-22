# Pathfinder

● Shortest Path Finder using BFS (Breadth-First Search)


📖 Overview
This project is a classic pathfinding solver implemented in Python using the curses library for a text-based, visual simulation. It employs the Breadth-First Search (BFS) algorithm to guarantee the discovery of the shortest possible path from a starting point (S) to a goal state (G) within a predefined, grid-based maze.
The maze traversal is visualized in the terminal, showing the search process step-by-step until the goal is reached, making it an excellent demonstration of how BFS works.


✨ Features
•	Shortest Path Guarantee: Uses BFS, which ensures the first path found is the shortest path in an unweighted graph (the maze).
•	Terminal Visualization: Displays the maze and the pathfinding process directly in the terminal using the curses library.
•	Step-by-Step Traversal: Visualizes the BFS exploration queue by highlighting current paths with an 'X' symbol.
•	Defined Maze Structure: Utilizes a simple 2D list to represent the maze grid, supporting walls (#), open space (""), start (S), and goal (G).


🛠 Technologies/Tools Used
•	Primary Language: Python 3
•	Algorithm: Breadth-First Search (BFS)
•	Visualization: Python's built-in curses 
•	Data Structures:
o	queue.Queue (for the BFS queue)
o	set (for the visited cells)
o	list (for storing the current path)


🚀 Steps to Install & Run the Project
Prerequisites
•	Python 3.x installed.
•	A terminal environment that supports curses (Standard on Linux/macOS. For Windows, you might need to use a compatible terminal like Windows Subsystem for Linux (WSL) or ensure windows-curses is installed).


Installation
1.	Save the code: Save the provided Python script as pathfinder.py.
2.	Install windows-curses (Windows only): If you are running this on a standard Windows Command Prompt or PowerShell, you need an alternative implementation:
3.	pip install windows-curses

Running the Application
1.	Execute the script: Open your terminal, navigate to the directory where you saved pathfinder.py, and run:
2.	python pathfinder.py
3.	Observe the Visualization: The maze will appear, and the search algorithm will begin tracing paths from 'S'.
4.	Exit: Once the path is found (or if no path exists), the application will pause. Press any key to close the program.


✅ Instructions for Testing
Since this project does not have automated unit tests, testing involves observing the visual output for correctness.
1.	Verify Shortest Path:
o	Run the script and observe the final path marked with 'X'.
o	Manually count the steps of the final path and confirm that it is indeed the minimum number of moves required from 'S' to 'G'.
2.	Test for No Path:
o	Edit the maze definition in pathfinder.py to surround 'G' completely with '#' walls.
o	Rerun the script and verify that the program correctly reports "No path found!" and the search stops.
3.	Test for Different Start/Goal Positions:
o	Change the location of 'S' and 'G' in the maze array.
o	Rerun the script to ensure the algorithm still finds the correct shortest path for the new configuration.


"""
Shortest path finder using BFS(Breadth First Search)
"""
import curses
from curses import wrapper
import time
import queue
maze = [
     ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', 'G', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]
"""
Here the # signifies bloked path and "" shows the space we can access
S is the starting point and G is the goal state
"""
def print_maze(maze,stdscr,path=[]):
 magenta=curses.color_pair(1)
 red=curses.color_pair(2)
 for i,row in enumerate(maze):
  for j,value in enumerate(row):
     if (i,j) in path:
      stdscr.addstr( i , j*2 ,  "X",magenta ) 
     else: 
      stdscr.addstr( i , j*2 ,  value,)
      #multiply by 2 to get more space

def find_start(maze,start):  
  for i,row in enumerate(maze):
   for j,value in enumerate(row):
    if value==start:
      return i, j
  return None

def find_path(maze, stdscr):
  start="S"
  end="G"
  start_pos=find_start(maze,start) 

  q=queue.Queue()#queue to carry out bfs
  q.put((start_pos, [start_pos]))
  
  visited=set()

  while not q.empty():
    current_pos,path=q.get()
    row,col=current_pos
    
    stdscr.clear()
    print_maze(maze,stdscr,path)
    time.sleep(0.3)
    stdscr.refresh()

    if maze[row][col]== end:
      return path
    
    neighbours=find_neighbour(maze, row, col)
    for neighbour in neighbours:
      if neighbour in visited:
        continue

      r,c=neighbour
      if maze[r][c]=="#":
        continue
      
      new_path= path + [neighbour]
      q.put((neighbour, new_path))
      visited.add(neighbour)


    

def find_neighbour(maze,row,col):
  neighbours=[]

  if row>0:
    neighbours.append((row-1,col))
  if row+1<len(maze):
    neighbours.append((row+1,col))
  if col>0:
    neighbours.append((row,col-1))
  if col+1<len(maze[0]):
    neighbours.append((row,col+1))
  return neighbours

  
def main(stdscr):#standard output screen as parameter
 curses.init_pair(1,curses.COLOR_MAGENTA,curses.COLOR_WHITE)
 curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLUE)
#INITIALIZE COLORS TO ADD COLOR TO THE MAZE 
 mag_white=curses.color_pair(1)
 red_blue=curses.color_pair(2)
 find_path(maze,stdscr)
 stdscr.getch() # helps control the  output 

wrapper(main)

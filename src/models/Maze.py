import random
from random import choice
from typing import Union
from models.Cell import Cell
from collections import deque
class Maze:
    # Class constructor
    def __init__(self) -> None:
        # Class attributes
        self.grid:list[list] = None
        self.rows:int = 0
        self.cols:int = 0
        self.start_cell:Cell = None
        self.end_cells:list = []
        self.current_cell:Cell = None
        self.next_cell:Cell = None
        self.stack:list = []
        self.queue:deque = deque()
        self.paths:list = []
        self.solutions:list = []

    # Grid attribute getter and setter methods
    def get_grid(self) -> list[list]:
        return self.grid
    def set_grid(self,grid:list[list]) -> None:
        self.grid = grid

    # Method that generates the maze grid
    def generate_grid(self) -> list[list]:
        grid:list[list] = []
        # Cycle that will generate the matrix needed for the maze
        # We start the cycle at 1 so that the amtrix is ​​drawn with clearance from the edge of the window
        for row in range(1,self.rows+1):
            grid_row:list = []
            for col in range(1,self.cols+1):
                cell:Cell = Cell(col, row)
                grid_row.append(cell)
            grid.append(grid_row)
        return grid
    
    # Rows attribute getter and setter methods
    def get_rows(self) -> int:
        return self.rows
    def set_rows(self,rows:int) -> None:
        self.rows = rows
        
    # Cols attribute getter and setter methods
    def get_cols(self) -> int:
        return self.cols
    def set_cols(self,cols:int) -> None:
        self.cols = cols
    
    # start_cell attribute getter and setter methods
    def get_start_cell(self) -> Cell:
        return self.start_cell
    def set_start_cell(self,cell:Cell) -> None:
        self.start_cell = cell
    
    # end_cell attribute getter, setter and other methods
    def get_end_cells(self) -> Cell:
        return self.end_cells
    def set_end_cells(self,list:list) -> None:
        self.end_cells = list
    
    def add_end_cells(self,cell:Cell)-> None:
        self.end_cells.append(cell)
    
    # current_cell attribute getter and setter methods
    def get_current_cell(self)-> Cell:
        return self.current_cell
    def set_current_cell(self,cell:Cell)->None:
        self.current_cell = cell
    
    # next_cell attribute getter and setter methods
    def get_next_cell(self)-> Cell:
        return self.next_cell
    def set_next_cell(self,cell:Cell)->None:
        self.next_cell = cell
        
    # paths attribute getter, setter and other methods
    def get_paths(self)->list:
        return self.paths
    def set_paths(self,list:list)->None:
        self.paths = list
        
    def add_paths(self,list:list)->None:
        self.paths.append(list)
    
    def add_element_path(self,cell:Cell,element:Cell)->None:
        for path in self.get_paths():
            if path[-1] == cell:
                path.append(element)

    def add_copy_path(self,cell:Cell,element:Cell)->None:
        paths = self.get_paths()
        for path in paths:
            if path[-2] == cell:
                temp_path:list = path[0:-1]
                temp_path.append(element)
                self.add_paths(temp_path)
                del temp_path
                break
        
    def remove_paths(self)->list:
        return self.stack.pop()
        
    # stack attribute getter, setter and other methods
    def get_stack(self)->list:
        return self.stack
    def set_stack(self,list:list)->None:
        self.stack = list
        
    def add_stack(self,cell:Cell)->None:
        self.stack.append(cell)
        
    def remove_stack(self)->Cell:
        return self.stack.pop()
    
    # queue attribute getter, setter and other methods
    def get_queue(self)->deque:
        return self.queue
    
    def set_queue(self,queue:deque)->None:
        self.queue = queue
        
    def add_queue(self,cell:Cell)->None:
        self.queue.append(cell)
    
    def remove_queue(self)->Cell:
        return self.get_queue().popleft()
    
    # solution attribute getter, setter and other methods
    def get_solutions(self) -> list:
        return self.solutions
    def set_solutions(self,solution:list) -> list:
        self.solutions = solution
        
    def add_solutions(self,list:list) -> None:
        self.solutions.append(list)
    
    # Metodo que irá definir as ultimas celulas
    def set_final_cells(self) -> None:
        # If the maze is greater than or equal to 15x15 then we can have zero, one or two final squares, if it is smaller we have zero or one final square
        number: int = random.randint(0, 2) if self.get_cols() * self.get_rows() >= 225 else random.randint(0, 1)
        # Assign a random final house in the 4th quadrant of the maze
        if number == 1: 
            self.add_end_cells(self.get_grid()[random.randint(self.get_rows()//2, self.get_rows()-1)][random.randint(self.get_cols()//2,self.get_cols()-1)])
        # If the maze is going to have more than one final square then we have to ensure that it does not land on exactly the same square
        # To do this, we define the first one and then check if the random numbers you gave us for the first one are not the same in the second one
        elif number == 2:
            start_end_1:int = random.randint(self.get_rows()//2, self.get_rows()-1)
            final_end_1:int = random.randint(self.get_cols()//2,self.get_cols()-1)
            self.add_end_cells(self.get_grid()[start_end_1][final_end_1]) # 1ª End_cell
            start_end_2:int = random.randint(self.get_rows()//2, self.get_rows()-1)
            final_end_2:int = random.randint(self.get_cols()//2,self.get_cols()-1)
            while start_end_1 == start_end_2 and final_end_1 == final_end_2: # Only enter if the cell is the same
                start_end_2 = random.randint(self.get_rows()//2, self.get_rows()-1)
                final_end_2 = random.randint(self.get_cols()//2,self.get_cols()-1)
            self.add_end_cells(self.get_grid()[start_end_2][final_end_2]) # 2ª end_cell
            
            
        
    # Method that will generate the maze itself 
    def generate_maze(self) -> 'Maze':
        self.set_end_cells([])
        self.set_current_cell(self.get_grid()[0][0])
        # Loop until there are no more unvisited cells
        while True: 
            self.get_current_cell().set_visited(True) # Mark the current cell as visited
            self.get_current_cell().set_neighbors(self.get_current_cell().check_neighbors_generate_maze(self.get_grid()))
            # Get the next unvisited neighbor. If there is more than one we choose randomly
            self.set_next_cell(choice(self.get_current_cell().get_neighbors())) if self.get_current_cell().get_neighbors() else self.set_next_cell(None)
            if self.get_next_cell(): # If there is an unvisited neighbor
                self.get_next_cell().set_visited(True) # Mark the next cell as visited
                self.add_stack(self.get_current_cell()) # Add the current cell to the stack
                self.get_current_cell().remove_walls(self.get_next_cell()) # Remove the walls between the current and next cell
                self.set_current_cell(self.get_next_cell())  # Move to the next cell
            elif self.get_stack(): # If the stack is not empty
                self.set_current_cell(self.remove_stack()) # Move back to the previous cell
            else:
                break # Exit the loop when there are no more unvisited cells
            
        # Assign a random starting house in the 1st quadrant of the maze
        self.set_start_cell(self.get_grid()[random.randint(0, self.get_rows()//2)][random.randint(0,self.get_cols()//2)])

        # Assign the final cells to the maze
        self.set_final_cells()
        
        # Clear all visited attributes of each maze cell for future use in the search for resolution
        self.clear_visited_attribute()
        
        # Clear all variables used
        self.get_current_cell().set_neighbors(None)
        self.set_current_cell(None)
        self.set_stack([])
        self.set_next_cell(None)
        
        return self
    
    # Method to clear all visited houses in the maze
    def clear_visited_attribute(self) -> None:
        # Clear all visited attributes of each maze cell for future use in the search for resolution
        temp_grid:list[list] = self.get_grid() # Temporary variable to store the current grid
        for row in range(0,self.rows):            
            for col in range(0,self.cols):
                temp_grid[row][col].set_visited(False)
        self.set_grid(temp_grid)
        del temp_grid # Free memory by deleting temporary variable
                
    # Method that starts the Breadth Search algorithm
    def first_fase_breadth(self) -> None:
        self.set_solutions([]) # Clear the solutions variable
        self.add_queue(self.get_start_cell()) # add the initial cell to the queue
        self.add_paths([self.get_start_cell()]) # add to path list
    
    # Method that will explore the entire maze trying to find all the paths from the beginning to the destination, destinations or void
    def second_fase_breadth(self) -> Union['Cell',None]:
        self.set_current_cell(self.remove_queue())
        self.get_current_cell().set_visited(True) # Mark the current cell as visited
        # We get all the neighbors that have not yet been visited of the current cell
        self.get_current_cell().set_neighbors(self.get_current_cell().check_neighbors_breadth_algorithm(self.get_grid())) 
        #This piece of code creates all possible paths from the current cell in the maze. If more than one neighbor is available, we add the first neighbor to the existing path. 
        # For subsequent neighbors, we copy the current path, excluding the last element (which is already the current neighbor), and add the neighbor under consideration. 
        # This process is repeated for each neighbor, ensuring that we explore all path options from the current cell.        
        for neighbor_cell in self.get_current_cell().get_neighbors():
            if neighbor_cell == self.get_current_cell().get_neighbors()[0]: 
                self.add_element_path(self.get_current_cell(), neighbor_cell)
            else:
                self.add_copy_path(self.get_current_cell(), neighbor_cell)
            self.add_queue(neighbor_cell)
                               
        # If the queue still has elements we need to do some checks
        if len(self.get_queue()) != 0:
            # If the next cell is the final one then we save this path as a solution
            if self.get_queue()[0] in self.get_end_cells():
                self.save_solution()
                # If all the necessary solutions have already been found, then we return these
                if len(self.get_solutions()) == len(self.get_end_cells()):
                    self.clear_visited_attribute() # Clear all visited attributes
                    self.clear_breadth_variables()
                    return self.get_solutions()
                return None
            # we return the next one to be seen
            else:
                return self.get_queue()[0]
        # If the queue is empty then all the houses have already been explored, we return all the paths found so far
        else:
            self.clear_visited_attribute() # Clear all visited attributes
            self.clear_breadth_variables() # Clear all variables used
            return self.get_solutions()  # return solutions
    
    # Method that resets all variables used in the breadth search method
    def clear_breadth_variables(self) -> None:
        self.get_current_cell().set_neighbors(None)
        self.set_current_cell(None)
        self.set_queue(deque())
        self.set_next_cell(None)
        self.set_paths([])
        
    # Method of the Breadth algorithm that aims to save the atual solution
    def save_solution(self):
        for path in self.get_paths():
            # If the path contains one of the final cells of the maze and that path has not already been saved in the list of solutions
            if path[-1] in self.get_end_cells() and path not in self.get_solutions(): 
                # We save a copy of that path using the slicing technique
                self.add_solutions(path[:])              
                break       

            
        
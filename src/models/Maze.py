import random
from random import choice
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
        self.end_cell:Cell = None
        self.current_cell:Cell = None
        self.next_cell:Cell = None
        self.neighbors:list = None
        self.stack:list = []
        self.queue:deque = None
        self.solution:list = None

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
    
    # end_cell attribute getter and setter methods
    def get_end_cell(self) -> Cell:
        return self.end_cell
    def set_end_cell(self,cell:Cell) -> None:
        self.end_cell = cell
    
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
        
    # neighbors attribute getter and setter methods
    def get_neighbors(self)->list:
        return self.neighbors
    
    def set_neighbors(self,list:list)->None:
        self.neighbors = list
        
    def add_neighbor(self,cell:Cell)->None:
        self.neighbors.append(cell)
        
    # stack attribute getter and setter methods
    def get_stack(self)->list:
        return self.stack
    
    def set_stack(self,list:list)->None:
        self.stack = list
        
    def add_stack(self,cell:Cell)->None:
        self.stack.append(cell)
        
    def remove_stack(self)->Cell:
        return self.stack.pop()
    
    # queue attribute getter and setter methods
    def get_queue(self)->deque:
        return self.queue
    
    def set_queue(self,queue:deque)->None:
        self.queue = queue
        
    def add_queue(self,cell:Cell)->None:
        self.queue.append(cell)
    
    def remove_queue(self)->Cell:
        return self.queue.popleft()
    
    # solution attribute getter and setter methods
    def get_solution(self) -> list:
        return self.solution
    
    def set_solution(self,solution:list) -> list:
        self.solution = solution
        
    def add_solution(self,cell:Cell) -> None:
        self.solution.append(cell)
    
    
    # Method that will generate the maze itself
    def generate_maze(self) -> 'Maze':
        self.set_current_cell(self.get_grid()[0][0])
        # Loop until there are no more unvisited cells
        while True: 
            self.get_current_cell().set_visited(True) # Mark the current cell as visited
            self.set_neighbors(self.get_current_cell().check_neighbors(self.get_grid()))
            # Get the next unvisited neighbor. If there is more than one we choose randomly
            self.set_next_cell(choice(self.get_neighbors())) if self.get_neighbors() else self.set_next_cell(None)
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
            # Assign a random final house in the 4th quadrant of the maze
            self.set_end_cell(self.get_grid()[random.randint(self.get_rows()//2, self.get_rows()-1)][random.randint(self.get_cols()//2,self.get_cols()-1)])
        
        # Clear all visited attributes of each maze cell for future use in the search for resolution
        temp_grid:list[list] = self.get_grid() # Temporary variable to store the current grid
        for row in range(0,self.rows):            
            for col in range(0,self.cols):
                temp_grid[row][col].set_visited(False)
        
        # Clear all variables used
        self.set_grid(temp_grid)
        del temp_grid # Free memory by deleting temporary variable
        self.set_current_cell(None)
        self.set_neighbors(None)
        self.set_stack([])
        self.set_next_cell(None)
        
        return self
    
    #################################################################################################################
    def first_fase_breadth(self) -> None:
        self.add_queue(self.get_start_cell())
    
    def second_fase_breadth(self):
        self.set_current_cell(self.remove_queue())
        self.get_current_cell().set_visited(True) # Mark the current cell as visited
        
        
        
        self.set_neighbors(self.get_current_cell().check_neighbors(self.get_grid()))
        # Get the next unvisited neighbor. If there is more than one we choose randomly
        self.set_next_cell(choice(self.get_neighbors())) if self.get_neighbors() else self.set_next_cell(None)
        if self.get_next_cell(): # If there is an unvisited neighbor
            self.get_next_cell().set_visited(True) # Mark the next cell as visited
            self.add_stack(self.get_current_cell()) # Add the current cell to the stack
            self.get_current_cell().remove_walls(self.get_next_cell()) # Remove the walls between the current and next cell
            self.set_current_cell(self.get_next_cell())  # Move to the next cell
        elif self.get_stack(): # If the stack is not empty
            self.set_current_cell(self.remove_stack()) # Move back to the previous cell
        else:
            pass
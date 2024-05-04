import random
from random import choice
from models.Cell import Cell
class Maze:
    # Class constructor
    def __init__(self) -> None:
        # Class attributes
        self.grid:list[list] = None
        self.rows:int = 0
        self.cols:int = 0
        self.start_cell:Cell = None
        self.end_cell:Cell = None
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
        
    # solution attribute getter and setter methods
    def get_solution(self) -> list:
        return self.solution
    
    def set_solution(self,solution:list) -> list:
        self.solution = solution
        
    def add_solution(self,cell:Cell) -> None:
        self.solution.append(cell)
    
    # Method that will generate the maze itself
    def generate_maze(self) -> 'Maze':
        current_cell:Cell = self.get_grid()[0][0]
        # Empty stack where all the cells that are going to be visited will be added
        stack:list = []
        # Loop until there are no more unvisited cells
        while True:
            current_cell.set_visited(True) # Mark the current cell as visited
            neighbors:list = current_cell.check_neighbors(self.get_grid())
            # Get the next unvisited neighbor. If there is more than one we choose randomly
            next_cell:Cell = choice(neighbors) if neighbors else False 
            if next_cell: # If there is an unvisited neighbor
                next_cell.set_visited(True) # Mark the next cell as visited
                stack.append(current_cell) # Add the current cell to the stack
                current_cell.remove_walls(next_cell) # Remove the walls between the current and next cell
                current_cell = next_cell  # Move to the next cell
            elif stack: # If the stack is not empty
                current_cell = stack.pop() # Move back to the previous cell
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
        self.set_grid(temp_grid)
        del temp_grid # Free memory by deleting temporary variable
        
        return self
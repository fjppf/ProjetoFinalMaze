import random
from models import Cell
class Maze:
    # Class constructor
    def __init__(self):
        # Class attributes
        self.grid:list = []
        self.rows:int = 0
        self.cols:int = 0
        self.start_cell:Cell = None
        self.end_cell:Cell = None

    # Grid attribute getter method
    def get_grid(self):
        return self.grid
    # Grid attribute setter method
    def set_grid(self,grid:list[list]):
        self.grid = grid

    # Method that generates the maze grid
    def generate_grid(self):
        grid = []
        # Cycle that will generate the matrix needed for the maze
        # We start the cycle at 1 so that the amtrix is ​​drawn with clearance from the edge of the window
        for row in range(1,self.rows+1):
            grid_row = []
            for col in range(1,self.cols+1):
                cell = Cell.Cell(col, row)
                grid_row.append(cell)
            grid.append(grid_row)
        return grid
    
    # Rows attribute getter method
    def get_rows(self):
        return self.rows
    # Rows attribute setter method
    def set_rows(self,rows:int):
        self.rows = rows
        
    # Cols attribute getter method
    def get_cols(self):
        return self.cols
    # Cols attribute setter method  
    def set_cols(self,cols:int):
        self.cols = cols
    
    # start_cell attribute getter method
    def get_start_cell(self):
        return self.start_cell
    # start_cell attribute setter method
    def set_start_cell(self,cell:Cell):
        self.start_cell = cell
    
    # end_cell attribute getter method
    def get_end_cell(self):
        return self.end_cell
    # end_cell attribute setter method
    def set_end_cell(self,cell:Cell):
        self.end_cell = cell
    
    # Method that will generate the maze itself
    def generate_maze(self):
        current_cell:Cell = self.get_grid()[0][0]
        stack:list = []
        while True:
            current_cell.set_visited(True)
            next_cell:Cell = current_cell.check_neighbors(self.get_grid()) ####### MISS COMENTS HERE ####################
            if next_cell: 
                next_cell.set_visited(True)
                stack.append(current_cell)
                current_cell.remove_walls(next_cell)
                current_cell = next_cell      
            elif stack:
                current_cell = stack.pop()   
            else:
                break
            
            # Assign a random starting house in the 1st quadrant of the maze
            self.set_start_cell(self.get_grid()[random.randint(0, self.get_rows()//2)][random.randint(0,self.get_cols()//2)])
            # Assign a random final house in the 4th quadrant of the maze
            self.set_end_cell(self.get_grid()[random.randint(self.get_rows()//2, self.get_rows()-1)][random.randint(self.get_cols()//2,self.get_cols()-1)])
        
        # Clear all visited attributes of each maze cell for future use in the search for resolution ############### verificar
        temp_grid:list[list] = self.get_grid() # Temporary variable to store the current grid
        for row in range(0,self.rows):            
            for col in range(0,self.cols):
                temp_grid[row][col].set_visited(False)
        self.set_grid(temp_grid)
        del temp_grid # Free memory by deleting temporary variable
        
        return self
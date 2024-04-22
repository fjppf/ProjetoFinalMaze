import random
from models import Cell
class Maze:
    # Class constructor
    def __init__(self):
        # Class attributes
        self.grid:list = []
        self.rows = 0
        self.cols = 0
        self.start_cell = None
        self.end_cell = None

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
    
        
    def set_rows(self,rows):
        self.rows = rows
        
    def get_rows(self):
        return self.rows
    
    def set_cols(self,cols):
        self.cols = cols
        
    def get_cols(self):
        return self.cols
    
    def set_start_cell(self,cell:Cell):
        self.start_cell = cell
        
    def get_start_cell(self):
        return self.start_cell
    
    def set_end_cell(self,cell:Cell):
        self.end_cell = cell
        
    def get_end_cell(self):
        return self.end_cell
    
    def generate_maze(self):
        current_cell = self.get_grid()[0][0]
        stack = []
        while True:
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(self.get_grid())
            if next_cell: 
                next_cell.visited = True
                stack.append(current_cell)
                current_cell.remove_walls(next_cell)
                current_cell = next_cell      
            elif stack:
                current_cell = stack.pop()   
            else:
                break
            
            self.set_start_cell(self.get_grid()[random.randint(0, self.get_rows()//2)][random.randint(0,self.get_cols()//2)])
            self.set_end_cell(self.get_grid()[random.randint(self.get_rows()//2, self.get_rows()-1)][random.randint(self.get_cols()//2,self.get_cols()-1)])
        
        
        return self
    
# o algoritmo do Francis a mostra o labirinto a ser criado tem de estar aqui ou pode mostrar as versoes antigas
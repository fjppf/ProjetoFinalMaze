from typing import Union
class Cell:
    # Class constructor
    def __init__(self,x,y) -> None:
        # Class attributes
        self.x:int = x 
        self.y:int = y 
        self.size:int = 20 
        self.walls:dict = {"top": True, "right": True, "bottom": True, "left": True} 
        self.visited:bool = False 
        self.neighbors:list = []

    # x attribute getter and setter methods
    def get_x(self) -> int:
        return self.x
    def set_x(self,x:int) -> None:
        self.x = x

    # y attribute getter and setter methods
    def get_y(self) -> int:
        return self.y
    def set_y(self,y:int) -> None:
        self.y = y
    
    # size attribute getter and setter methods
    def get_size(self) -> int:
        return self.size
    def set_size(self,size:int) -> None:
        self.size = size
    
    # walls attribute getter and setter methods
    def get_wall(self,direction:str) -> str:
        return self.walls[direction]
    def set_wall(self,direction:str,value:bool) -> None:
        self.walls[direction] = value
    
    # visited attribute getter and setter methods
    def get_visited(self) -> bool:
        return self.visited
    def set_visited(self,visited:bool) -> None:
        self.visited = visited
    
    # neighbors attribute getter, setter and other methods
    def get_neighbors(self)->list:
        return self.neighbors
    def set_neighbors(self,list:list)->None:
        self.neighbors = list
        
    def add_neighbor(self,cell:'Cell')->None:
        self.neighbors.append(cell)
    
    # Method that see which square is currently in and returns the same
    def check_cell(self, x:int, y:int,grid:list[list]) -> Union['Cell',None]:
        for row in grid:
            for cell in row:
                if cell.get_x() == x and cell.get_y() == y: return cell
        return None
    
    # Method that sees which neighbors are available and chooses one to follow
    def check_neighbors_generate_maze(self,grid:list[list]) -> 'Cell':
        neighbors:list = []
        # Check the top neighbor
        top:Cell = self.check_cell(self.get_x(), self.get_y()-1,grid)
        # Check the right neighbor
        right:Cell = self.check_cell(self.get_x() + 1, self.get_y(),grid)
        # Check the bottom neighbor
        bottom:Cell = self.check_cell(self.get_x(), self.get_y() + 1,grid)
        # Check the left neighbor
        left:Cell = self.check_cell(self.get_x() - 1, self.get_y(),grid)

        # If there is a cell on top/right/bottom/left of the current cell, and that cell(top/right/bottom/left) it's not visited 
        # gets added to the list.
        if top and not top.get_visited():
            neighbors.append(top)
        if right and not right.get_visited():
            neighbors.append(right)
        if bottom and not bottom.get_visited(): 
            neighbors.append(bottom)
        if left and not left.get_visited(): 
            neighbors.append(left)
        return neighbors
    
    # Method that remove the walls from the cells
    def remove_walls(self, next:'Cell') -> None:
        # Calculate the difference in x coordinates between the current cell and the next cell
        dx:int = self.x - next.x
        # If the difference is 1 (indicating next cell is to the left of current cell)
        if dx == 1:
            self.set_wall('left',False) # In the current cell removes the left wall 
            next.set_wall('right',False) # In the next cell removes the right wall 
        # If the difference is -1 (indicating next cell is to the right of current cell)
        elif dx == -1:
            self.set_wall('right',False) # In the current cell removes the right wall 
            next.set_wall('left',False) # In the next cell removes the left wall 
        # Calculate the difference in y coordinates between the current cell and the next cell
        dy:int = self.y - next.y
        # If the difference is 1 (indicating next cell is above the current cell)
        if dy == 1:
            self.set_wall('top',False) # In the current cell removes the top wall 
            next.set_wall('bottom',False) # In the next cell removes the bottom wall 
        # If the difference is -1 (indicating next cell is below the current cell)
        elif dy == -1:
            self.set_wall('bottom',False) # In the current cell removes the bottom wall 
            next.set_wall('top',False) # In the next cell removes the top wall 
            
    # Method that sees which neighbors are available and chooses one to follow
    def check_neighbors_breadth_algorithm(self,grid:list[list]) -> 'Cell':
        neighbors:list = []
        # Check the top neighbor
        top:Cell = self.check_cell(self.get_x(), self.get_y()-1,grid)
        # Check the right neighbor
        right:Cell = self.check_cell(self.get_x() + 1, self.get_y(),grid)
        # Check the bottom neighbor
        bottom:Cell = self.check_cell(self.get_x(), self.get_y() + 1,grid)
        # Check the left neighbor
        left:Cell = self.check_cell(self.get_x() - 1, self.get_y(),grid)

        # If there is a cell on top/right/bottom/left of the current cell, and that cell(top/right/bottom/left) it's not visited 
        # gets added to the list.
        if top and not top.get_visited() and not top.get_wall("bottom"):
            neighbors.append(top)
        if right and not right.get_visited() and not right.get_wall("left"):
            neighbors.append(right)
        if bottom and not bottom.get_visited() and not bottom.get_wall("top"): 
            neighbors.append(bottom)
        if left and not left.get_visited() and not left.get_wall("right"): 
            neighbors.append(left)
        return neighbors
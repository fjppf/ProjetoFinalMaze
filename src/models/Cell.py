from random import choice
import pygame 

class Cell:
    # Class constructor
    def __init__(self,x,y):
        # Class attributes
        self.x:int = x 
        self.y:int = y 
        self.size:int = 20 
        self.walls:dict = {"top": True, "right": True, "bottom": True, "left": True} 
        self.visited:bool = False 

    # x attribute getter and setter methods
    def get_x(self):
        return self.x
    def set_x(self,x):
        self.x = x

    # y attribute getter and setter methods
    def get_y(self):
        return self.y
    def set_y(self,y):
        self.y = y
    
    # size attribute getter and setter methods
    def get_size(self):
        return self.size
    def set_size(self,size):
        self.size = size
    
    # walls attribute getter and setter methods
    def get_wall(self,direction):
        return self.walls[direction]
    def set_wall(self,direction,value):
        self.walls[direction] = value
    
    # visited attribute getter and setter methods
    def get_visited(self):
        return self.visited
    def set_visited(self,visited):
        self.visited = visited
    
    def check_cell(self, x, y,grid):#ver qual é o quadrado que esta no momento
        for row in grid:
            for cell in row:
                if cell.get_x() == x and cell.get_y() == y: return cell
        return None
    

    def check_neighbors(self,grid):
        neighbors = []
        # Check the top neighbor
        top = self.check_cell(self.get_x(), self.get_y()-1,grid)
        # Check the right neighbor
        right = self.check_cell(self.get_x() + 1, self.get_y(),grid)
        # Check the bottom neighbor
        bottom = self.check_cell(self.get_x(), self.get_y() + 1,grid)
        # Check the left neighbor
        left = self.check_cell(self.get_x() - 1, self.get_y(),grid)

        # If there is a cell on top/right/bottom/left of the current cell, 
        #and that cell(top/right/bottom/left) it's not visited gets added to the list
        if top and not top.get_visited():
            neighbors.append(top)
        if right and not right.get_visited():
            neighbors.append(right)
        if bottom and not bottom.get_visited(): 
            neighbors.append(bottom)
        if left and not left.get_visited(): 
            neighbors.append(left)
        return choice(neighbors) if neighbors else False 
    
    # If the list is empty return a false value
    def remove_walls(self, next):
        dx:int = self.x - next.x
        if dx == 1:
            self.set_wall('left',False)
            next.set_wall('right',False) ##################### MISS COMMENTS #################################
        elif dx == -1:
            self.set_wall('right',False)
            next.set_wall('left',False)
        dy:int = self.y - next.y
        if dy == 1:
            self.set_wall('top',False)
            next.set_wall('bottom',False)
        elif dy == -1:
            self.set_wall('bottom',False)
            next.set_wall('top',False)
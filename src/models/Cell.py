from random import choice
import pygame 

class Cell:
    
    def __init__(self,x,y):
        self.x:int = x # Coordinate x
        self.y:int = y # Coordinate y
        self.size:int = 20 # Cell size
        self.walls:dict = {"top": True, "right": True, "bottom": True, "left": True} # Walls
        self.visited:bool = False # Cell status check variable

    
    def get_x(self):
        return self.x
    def set_x(self,x):
        self.x = x

    def get_y(self):
        return self.y
    def set_y(self,y):
        self.y = y
        
    def get_size(self):
        return self.size
    def set_size(self,size):
        self.size = size
    
    def get_wall(self,direction):
        return self.walls[direction]
    def set_wall(self,direction,value):
        self.walls[direction] = value
    
    def get_visited(self):
        return self.visited
    def set_visited(self,visited):
        self.visited = visited


    def draw_cell(self,screen,color):
        x:int = self.get_x() * self.get_size() # Stores the x coordinate of the cell on the screen
        y:int = self.get_y() * self.get_size() # Stores the y coordinate of the cell on the screen
        
        # Drawing the cell on the screen
        pygame.draw.rect(screen, pygame.Color(color),(x,y,self.get_size(), self.get_size())) # (x-coordinate of the top-left corner,y-coordinate of the top-left corner,widht, heght)

    def draw(self, screen): #desenhar a grid
        x:int = self.get_x() * self.get_size() # Stores the x coordinate of the cell on the screen
        y:int = self.get_y() * self.get_size() # Stores the y coordinate of the cell on the screen
        
        # Drawing the cell on the screen
        pygame.draw.rect(screen, pygame.Color("black"),(x,y,self.get_size(), self.get_size()))# (x-coordinate of the top-left corner,y-coordinate of the top-left corner,widht, heght)

        if self.get_wall('top'):#desenhar as paredes do topo do quadrado 
            pygame.draw.line(screen, pygame.Color('darkorange'), (x, y), (x + self.get_size(), y)) #line(surface, color, start_pos, end_pos)
        if self.get_wall('right'):#desenhar as paredes da direita do quadrado 
            pygame.draw.line(screen, pygame.Color('darkorange'), (x + self.get_size(), y), (x + self.get_size(), y + self.get_size()))
        if self.get_wall('bottom'):#desenhar as paredes de baixo do quadrado 
            pygame.draw.line(screen, pygame.Color('darkorange'), (x + self.get_size(), y + self.get_size()), (x , y + self.get_size()))
        if self.get_wall('left'):#desenhar as paredes da esquerda do quadrado 
            pygame.draw.line(screen, pygame.Color('darkorange'), (x, y + self.get_size()), (x, y))

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

        #if there is a cell on top/right/bottom/left of the current cell, 
        #and that cell(top/right/bottom/left) it's not visited gets added to the list

        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited: 
            neighbors.append(bottom)
        if left and not left.visited: 
            neighbors.append(left)
        return choice(neighbors) if neighbors else False 
    
    #if the list is empty return a flase value
    def remove_walls(self, next):
        dx:int = self.x - next.x
        if dx == 1:
            self.set_wall('left',False)
            next.set_wall('right',False)
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
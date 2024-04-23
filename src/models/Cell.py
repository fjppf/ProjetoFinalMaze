from random import choice
import pygame 

class Cell:

    def __init__(self,x,y):
        self.x = x #cordenada x
        self.y = y #cordenada y
        self.size = 20 #tamanho da celula
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}#paredes
        self.visited = False#estado se o quadrado foi visitado

    
    def get_x(self):
        return self.x
    def set_x(self,x):
        self.x = x

    def get_y(self):
        return self.y
    def set_y(self,y):
        self.y = y
    
    #falta o get/set do  atributo walls
    
    def get_visited(self):
        return self.visited
    def set_visited(self,visited):
        self.visited = visited


    def draw_cell(self,screen,color):
        x = self.get_x() * self.size #coordenada x * tamanho do quadrado
        y = self.get_y() * self.size#coordenada y * tamanho do quadrado
        pygame.draw.rect(screen, pygame.Color(color),(x,y,self.size, self.size))# (x-coordinate of the top-left corner,y-coordinate of the top-left corner,widht, heght)

    def draw(self, screen): #desenhar a grid
        x = self.get_x() *self.size
        y = self.get_y() *self.size
        
        pygame.draw.rect(screen, pygame.Color("black"),(x,y,self.size, self.size))# (x-coordinate of the top-left corner,y-coordinate of the top-left corner,widht, heght)

        if self.walls['top']:#desenhar as paredes do topo do quadrado 
            pygame.draw.line(screen, pygame.Color('darkorange'), (x, y), (x + self.size, y)) #line(surface, color, start_pos, end_pos)
        if self.walls['right']:#desenhar as paredes da direita do quadrado 
            pygame.draw.line(screen, pygame.Color('darkorange'), (x + self.size, y), (x + self.size, y + self.size))
        if self.walls['bottom']:#desenhar as paredes de baixo do quadrado 
            pygame.draw.line(screen, pygame.Color('darkorange'), (x + self.size, y + self.size), (x , y + self.size))
        if self.walls['left']:#desenhar as paredes da esquerda do quadrado 
            pygame.draw.line(screen, pygame.Color('darkorange'), (x, y + self.size), (x, y))

    def check_cell(self, x, y,grid):#ver qual é o quadrado que esta no momento
        for row in grid:
            for cell in row:
                if cell.get_x() == x and cell.get_y() == y: return cell
        return None
    

    def check_neighbors(self,grid):
        neighbors = []
        top = self.check_cell(self.get_x(), self.get_y()-1,grid)
        right = self.check_cell(self.get_x() + 1, self.get_y(),grid)
        bottom = self.check_cell(self.get_x(), self.get_y() + 1,grid)
        left = self.check_cell(self.get_x() - 1, self.get_y(),grid)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited: ############## usar o get_visited de cada celula nao aceder diretamente ao atributo
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False
    
    def remove_walls(self, next):
        dx = self.x - next.x
        if dx == 1:
            self.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            self.walls['right'] = False
            next.walls['left'] = False
        dy = self.y - next.y
        if dy == 1:
            self.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            self.walls['bottom'] = False
            next.walls['top'] = False
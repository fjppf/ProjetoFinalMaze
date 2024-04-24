import pygame
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
import pygame_widgets
class view:
    def __init__(self,controller):
        self.view_controller = controller
        self.screen = pygame.display.set_mode((1400, 850))
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption("Maze Game")
        
        self.text_font:pygame.font= pygame.font.SysFont("Arial",20)
        self.title_font:pygame.font = pygame.font.SysFont("Arial Black",30)
        self.color_black:tuple=(0, 0, 0)
        self.draw_titles("Maze Problem", self.title_font,self.color_black,950,30)
        self.draw_titles("Create Maze", self.title_font,self.color_black,970,100)
        self.draw_labels("Number of columns:", self.text_font,self.color_black,820,155)
        self.draw_labels("Number of rows:", self.text_font,self.color_black,820,205)
        self.draw_titles("Options", self.title_font,self.color_black,1000,430)

        self.txtNumbCols = TextBox(self.screen, 970, 150, 200, 40, fontSize=20, borderColour=(255, 0, 0), textColour=(0, 200, 0))
        self.txtNumbRowss = TextBox(self.screen, 970, 200, 200, 40, fontSize=20, borderColour=(255, 0, 0), textColour=(0, 200, 0))

        cBtn = pygame.image.load("src/images/button_create.png").convert()   
        self.createBtn = Button(self.screen, 990, 280, 173, 60, radius=0, onClick=self.draw_maze, image=cBtn)
        sBtn = pygame.image.load("src/images/button_solve.png").convert()   
        self.solveBtn = Button(self.screen, 990, 360, 173, 60, radius=0, onClick=self.clear_grid, image=sBtn)

        clBtn = pygame.image.load("src/images/button_clear-maze.png").convert()  
        self.clearBtn = Button(self.screen, 900, 500, 173, 30, radius=50, onClick=self.clear_grid, image=clBtn)

        brBtn = pygame.image.load("src/images/button_breadth-algorithm.png").convert()  
        self.breadthBtn = Button(self.screen, 1100, 500, 173, 30, radius=50, onClick=self.clear_grid, image=brBtn)

        daBtn = pygame.image.load("src/images/button_depth-algorithm.png").convert()  
        self.depthBtn = Button(self.screen, 900, 600, 173, 30, radius=50, onClick=self.clear_grid, image=daBtn)

        asBtn = pygame.image.load("src/images/button_depth-algorithm.png").convert()  
        self.aBtn = Button(self.screen, 1100, 600, 173, 30, radius=50, onClick=self.clear_grid, image=asBtn)
        
        events = pygame.event.get()
    
        pygame_widgets.update(events)
        pygame.display.update()#updates the display
        
    def draw_cell(self,cell, bg_color, wl_color): #desenhar a grid
        x:int = cell.get_x() * cell.get_size() # Stores the x coordinate of the cell on the screen
        y:int = cell.get_y() * cell.get_size() # Stores the y coordinate of the cell on the screen
        
        # Drawing the cell on the screen
        pygame.draw.rect(self.screen, pygame.Color(bg_color),(x,y,cell.get_size(), cell.get_size()))

        # The following code checks which walls the cell is supposed to have by checking the walls attribute 
        # of the respective cell and, if so, draw it on the screen using pygame.draw.line
        if cell.get_wall('top'):
            pygame.draw.line(self.screen, pygame.Color(wl_color), (x, y), (x + cell.get_size(), y)) #line(surface, color, start_pos, end_pos)
        if cell.get_wall('right'):
            pygame.draw.line(self.screen, pygame.Color(wl_color), (x + cell.get_size(), y), (x + cell.get_size(), y + cell.get_size()))
        if cell.get_wall('bottom'):
            pygame.draw.line(self.screen, pygame.Color(wl_color), (x + cell.get_size(), y + cell.get_size()), (x , y + cell.get_size()))
        if cell.get_wall('left'):
            pygame.draw.line(self.screen, pygame.Color(wl_color), (x, y + cell.get_size()), (x, y))
            
    def draw_maze(self):
        #verificação do tamanho das colunas e linhas
        self.screen.fill((255, 255, 255))
        self.maze = self.view_controller.generate_maze(int(self.txtNumbRowss.getText()),int(self.txtNumbCols.getText()))
        for row in self.maze.get_grid():
            for cell in row:
                self.draw_cell(cell,"black","darkorange")
        self.draw_cell(self.maze.get_start_cell(),"green","darkorange")
        self.draw_cell(self.maze.get_end_cell(),"red","darkorange")

        pygame.display.update()
    
    def draw_labels(self,text,font, color, x, y):
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface,(x,y))

    def draw_titles(self,text,font, color, x, y):
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface,(x,y))

    def clear_grid(self):
        print("hello")
    
    def update_ui(self):
        self.txtNumbCols.draw()
        self.txtNumbRowss.draw()
        self.createBtn.draw()
        self.solveBtn.draw()
        self.clearBtn.draw()
        self.breadthBtn.draw()
        self.depthBtn.draw()
        self.aBtn.draw()
        self.draw_titles("Maze Problem", self.title_font,self.color_black,950,30)
        self.draw_titles("Create Maze", self.title_font,self.color_black,970,100)
        self.draw_labels("Number of columns:", self.text_font,self.color_black,820,155)
        self.draw_labels("Number of rows:", self.text_font,self.color_black,820,205)
        self.draw_titles("Options", self.title_font,self.color_black,1000,430)

    
    

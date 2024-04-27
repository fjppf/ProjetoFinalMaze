import pygame
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
import pygame_widgets
class view:
    def __init__(self,controller):
        self.view_controller = controller
        # Obtém o tamanho do monitor principal
        screen_info = pygame.display.Info()
        self.screen_width = screen_info.current_w
        self.screen_height = screen_info.current_h
        # Definir a tela como fullscreen com a resolução obtida
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height-55))
    
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption("Maze Simulator")
        
        self.text_font:pygame.font= pygame.font.SysFont("Arial",20)
        self.title_font:pygame.font = pygame.font.SysFont("Arial Black",30)
        self.color_black:tuple=(0, 0, 0)
        self.draw_titles("Create Maze", self.title_font,self.color_black,self.screen_width-286.5,17)
        self.draw_labels("Number of columns:", self.text_font,self.color_black,self.screen_width-370,75)
        self.draw_labels("Number of rows:", self.text_font,self.color_black,self.screen_width-343,120)
        self.draw_titles("Options", self.title_font,self.color_black,1000,430)

        self.txtNumbCols = TextBox(self.screen, self.screen_width-212, 70, 200, 35, fontSize=20, borderColour=(255, 0, 0), textColour=(0, 200, 0))
        self.txtNumbRowss = TextBox(self.screen, self.screen_width-212, 115, 200, 35, fontSize=20, borderColour=(255, 0, 0), textColour=(0, 200, 0))

        cBtn = pygame.image.load("src/images/button_create.png").convert()   
        self.createBtn = Button(self.screen, self.screen_width-273, 280, 175, 60, radius=0, onClick=self.draw_maze, image=pygame.transform.scale(cBtn,(175,60)))
        sBtn = pygame.image.load("src/images/button_solve.png").convert()   
        self.solveBtn = Button(self.screen, self.screen_width-273, 360, 175, 60, radius=0, onClick=self.clear_grid, image=pygame.transform.scale(sBtn,(175,60)))

        clBtn = pygame.image.load("src/images/button_clear-maze.png").convert()  
        self.clearBtn = Button(self.screen, 900, 500, 175, 60, radius=50, onClick=self.clear_grid, image=pygame.transform.scale(clBtn,(175,60)))

        brBtn = pygame.image.load("src/images/button_breadth-algorithm.png").convert()  
        self.breadthBtn = Button(self.screen, 1100, 500, 175, 60, radius=50, onClick=self.clear_grid, image=pygame.transform.scale(brBtn,(175,60)))

        daBtn = pygame.image.load("src/images/button_depth-algorithm.png").convert()  
        self.depthBtn = Button(self.screen, 900, 600, 175, 60, radius=50, onClick=self.clear_grid, image=pygame.transform.scale(daBtn,(175,60)))

        asBtn = pygame.image.load("src/images/button_a-search-algorithm.png").convert()  
        self.aBtn = Button(self.screen, 1100, 600, 175, 60, radius=50, onClick=self.clear_grid, image=pygame.transform.scale(asBtn,(175,60)))
        
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
        self.screen.fill((255,255,255),pygame.Rect(0, 0, self.screen_width-370, self.screen_height)) 
        
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
        print("hola")
        self.screen.blit(text_surface,(x,y))

    def clear_grid(self):
        print("hello")

        

    
    

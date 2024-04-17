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

    def draw_maze(self):
        #verificação do tamanho das colunas e linhas
        self.screen.fill((255, 255, 255))
        self.maze = self.view_controller.generate_maze(int(self.txtNumbRowss.getText()),int(self.txtNumbCols.getText()))
        for row in self.maze.get_grid():
            for cell in row:
                cell.draw(self.screen)
        self.maze.get_start_cell().draw_cell(self.screen,"green")
        self.maze.get_end_cell().draw_cell(self.screen,"red")

        end_cell = self.maze.get_end_cell()
        pygame.display.update()
    
    def draw_labels(self,text,font, color, x, y):
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface,(x,y))

    def draw_titles(self,text,font, color, x, y):
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface,(x,y))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.view_controller.generate_maze()

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

    
    

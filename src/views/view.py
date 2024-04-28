import pygame
import pygame_gui
import pygame_gui.ui_manager
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
from views.picker_view import picker_view
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
        self.ui_manager = pygame_gui.UIManager((self.screen_width, self.screen_height-55))
        self.pickerView = picker_view(self.screen,self.ui_manager)
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption("Maze Simulator")
        
        self.text_font:pygame.font= pygame.font.SysFont("Arial",20)
        self.title_font:pygame.font = pygame.font.SysFont("Arial Black",30)
        self.color_black:tuple=(0, 0, 0)
        self.draw_labels("Create Maze", self.title_font,self.color_black,self.screen_width-286.5,17)
        self.draw_labels("Number of columns :", self.text_font,self.color_black,self.screen_width-370,75)
        self.txtNumbCols = TextBox(self.screen, self.screen_width-212, 70, 200, 35, fontSize=20, borderColour=(255, 0, 0), textColour=(0, 200, 0))
        
        self.draw_labels("Number of rows :", self.text_font,self.color_black,self.screen_width-343,120)
        self.txtNumbRowss = TextBox(self.screen, self.screen_width-212, 115, 200, 35, fontSize=20, borderColour=(255, 0, 0), textColour=(0, 200, 0))

        ###################################################################
        
        self.draw_labels("Walls color :", self.text_font,self.color_black,self.screen_width-306,170)
        self.current_color_wls = pygame.Color(255,140,0)
        # (tela onde o botão será desenhado, posição x do botão, posição y do botão, largura do botão, altura do botão, radius do botão, texto do botão, tamanho da fonte do texto, 
        # margem ao redor do texto, cor do botão quando inativo, cor do botão quando o mouse passa por cima, cor do botão quando clicado, função a ser chamada quando o botão é clicado, imagem de fundo do botão )
        self.pick_color_btn_wls = Button(self.screen,self.screen_width-192,165,100,35,radius=50,text='Pick color!',fontSize=20,margin=20,inactiveColour='red',hoverColour='green', pressedColour='black',onClick=self.pick_color_btn_wls_click)
        self.rect_wls = pygame.draw.rect(self.screen, self.current_color_wls, (self.screen_width-57, 165, 35, 35))
        
        self.draw_labels("Background color :", self.text_font,self.color_black,self.screen_width-353,220)
        self.current_color_bg = pygame.Color(0,0,0)
        self.pick_color_btn_bg = Button(self.screen,self.screen_width-192,215,100,35,radius=50,text='Pick color!',fontSize=20,margin=20,inactiveColour='red',hoverColour='green', pressedColour='black',onClick=self.pick_color_btn_bg_click)
        self.rect_bg = pygame.draw.rect(self.screen, self.current_color_bg, (self.screen_width-57, 215, 35, 35))
        
        
        #####################################################################
        
        create_Btn = pygame.image.load("src/images/button_create.png").convert()   
        self.createBtn = Button(self.screen, self.screen_width-370, 285, 175, 60, radius=0, onClick=self.create_btn_click, image=pygame.transform.scale(create_Btn,(175,60)))
        
        solve_Btn = pygame.image.load("src/images/button_solve.png").convert()   
        self.solveBtn = Button(self.screen, self.screen_width-185, 285, 175, 60, radius=0, onClick=self.clear_grid, image=pygame.transform.scale(solve_Btn,(175,60)))
        
        clear_Btn = pygame.image.load("src/images/button_create.png").convert()   
        self.clearBtn = Button(self.screen, self.screen_width-370, 365, 175, 60, radius=0, onClick=self.clear_btn_click, image=pygame.transform.scale(clear_Btn,(175,60)))
        
        save_Btn = pygame.image.load("src/images/button_solve.png").convert()   
        self.saveBtn = Button(self.screen, self.screen_width-185, 365, 175, 60, radius=0, onClick=self.clear_grid, image=pygame.transform.scale(save_Btn,(175,60)))
        
        self.draw_labels("Options", self.title_font,self.color_black,self.screen_width-248,455)
        
        lsBtn = pygame.image.load("src/images/button_clear-maze.png").convert()  
        self.lsearchbtn = Button(self.screen, self.screen_width-370, 508, 175, 60, radius=50, onClick=self.clear_grid, image=pygame.transform.scale(lsBtn,(175,60)))

        brBtn = pygame.image.load("src/images/button_breadth-algorithm.png").convert()  
        self.breadthBtn = Button(self.screen, self.screen_width-185, 508, 175, 60, radius=50, onClick=self.clear_grid, image=pygame.transform.scale(brBtn,(175,60)))

        daBtn = pygame.image.load("src/images/button_depth-algorithm.png").convert()  
        self.depthBtn = Button(self.screen, self.screen_width-370, 588, 175, 60, radius=50, onClick=self.clear_grid, image=pygame.transform.scale(daBtn,(175,60)))

        asBtn = pygame.image.load("src/images/button_a-search-algorithm.png").convert()  
        self.asearchBtn = Button(self.screen, self.screen_width-185, 588, 175, 60, radius=50, onClick=self.clear_grid, image=pygame.transform.scale(asBtn,(175,60)))
        
        events = pygame.event.get()
    
        pygame_widgets.update(events)
        pygame.display.update()#updates the display
    
    def pick_color_btn_wls_click(self):
        self.current_color_wls = self.pickerView.color_picker(self.current_color_wls,self)
        self.rect_wls = pygame.draw.rect(self.screen, self.current_color_wls, (self.screen_width-57, 165, 35, 35))
        self.clear_grid()
    
    def pick_color_btn_bg_click(self):
        self.current_color_bg = self.pickerView.color_picker(self.current_color_bg,self)
        self.rect_bg = pygame.draw.rect(self.screen, self.current_color_bg, (self.screen_width-57, 215, 35, 35))
        self.clear_grid()

    
    def create_btn_click(self):
        self.createBtn.disable()
        self.pick_color_btn_wls.disable()
        self.pick_color_btn_bg.disable()
        self.draw_maze()
    
    def solve_btn_click(self):
        pass
    
    def clear_btn_click(self):
        self.createBtn.enable()
        self.pick_color_btn_wls.enable()
        self.pick_color_btn_bg.enable()
        self.clear_grid()
        
    def save_btn_click(self):
        pass
        
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
        self.clear_grid()
        
        self.maze = self.view_controller.generate_maze(int(self.txtNumbRowss.getText()),int(self.txtNumbCols.getText()))
        for row in self.maze.get_grid():
            for cell in row:
                self.draw_cell(cell,self.current_color_bg,self.current_color_wls)
        self.draw_cell(self.maze.get_start_cell(),"green",self.current_color_wls)
        self.draw_cell(self.maze.get_end_cell(),"red",self.current_color_wls)

        pygame.display.update()
        
    def draw_labels(self,text,font, color, x, y):
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface,(x,y))

    def clear_grid(self):
        self.screen.fill((255,255,255),pygame.Rect(0, 0, self.screen_width-370, self.screen_height))

    







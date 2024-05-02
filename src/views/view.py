import pygame
import pygame_gui
import pygame_gui.ui_manager
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
from views.picker_view import picker_view
import pygame_widgets

class view:
    # Class constructor
    def __init__(self,controller) -> None:
        self.view_controller:'view_controller' = controller
        
        # Get the size of the main monitor
        screen_info:pygame.display = pygame.display.Info()
        self.screen_width:int = screen_info.current_w # Screen width
        self.screen_height:int = screen_info.current_h # Screen height
              
        # Set the screen to fullscreen with the obtained resolution
        self.screen:pygame.display = pygame.display.set_mode((self.screen_width, self.screen_height-55))
        self.ui_manager:pygame_gui.ui_manager = pygame_gui.UIManager((self.screen_width, self.screen_height-55))
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption("Maze Simulator")
        
        # Instantiate from color picker view
        self.pickerView:picker_view = picker_view(self.screen,self.ui_manager)
        
        # Desenhar os elementos na view
        self.text_font:pygame.font= pygame.font.SysFont("Arial",20) # Source of texts
        self.title_font:pygame.font = pygame.font.SysFont("Arial Black",30) # Source of titles
        self.color_black:tuple=(0, 0, 0) # Color use in texts
        # Draw title in view (title, font, color, x, y)
        self.draw_labels("Create Maze", self.title_font,self.color_black,self.screen_width-286.5,17)
        # Draw text in view
        self.draw_labels("Number of columns :", self.text_font,self.color_black,self.screen_width-370,75)
        # Draw textbox to insert the desired number of columns (screen, x, y, text width, text height, font size, border color, text color)        
        self.txtNumbCols:TextBox = TextBox(self.screen, self.screen_width-212, 70, 200, 35, fontSize=20, borderColour=(255, 0, 0), textColour=(0, 200, 0))
        # Draw text in view
        self.draw_labels("Number of rows :", self.text_font,self.color_black,self.screen_width-343,120)
        # Draw textbox to insert the desired number of columns
        self.txtNumbRowss:TextBox = TextBox(self.screen, self.screen_width-212, 115, 200, 35, fontSize=20, borderColour=(255, 0, 0), textColour=(0, 200, 0))
        # Draw text in view
        self.draw_labels("Walls color :", self.text_font,self.color_black,self.screen_width-306,170)
        
        # Below we have initialized the initial colors of both the background and the walls of the maze, and we also have an explanation of the button parameters
        # The rectangles serve to show the user which color is chosen in the picker and which will be used to create the maze
        self.current_color_wls:pygame.color = pygame.Color(255,140,0)
        # (screen where the button will be drawn, button x position, button y position, button width, button height, button radius, button text, text font size,
        # margin around text, button color when inactive, button color when mouse hovers over, button color when clicked, function to be called when button is clicked, button background image) 
        self.pick_color_btn_wls:Button = Button(self.screen,self.screen_width-192,165,100,35,radius=50,text='Pick color!',fontSize=20,margin=20,inactiveColour='red',hoverColour='green', pressedColour='black',onClick=self.pick_color_btn_wls_click)
        self.rect_wls:pygame.rect = pygame.draw.rect(self.screen, self.current_color_wls, (self.screen_width-57, 165, 35, 35))
        # Draw text in view
        self.draw_labels("Background color :", self.text_font,self.color_black,self.screen_width-353,220)
        self.current_color_bg:pygame.color = pygame.Color(0,0,0)
        self.pick_color_btn_bg:Button = Button(self.screen,self.screen_width-192,215,100,35,radius=50,text='Pick color!',fontSize=20,margin=20,inactiveColour='red',hoverColour='green', pressedColour='black',onClick=self.pick_color_btn_bg_click)
        self.rect_bg:pygame.rect = pygame.draw.rect(self.screen, self.current_color_bg, (self.screen_width-57, 215, 35, 35))
        
        # Design of the 4 main simulator buttons (Create, Solve, Clear, Save)
        # The background of each button will be an image created by us
        create_Btn_img:pygame.image = pygame.image.load("src/images/button_create.png").convert()   
        self.createBtn = Button(self.screen, self.screen_width-370, 285, 175, 60, radius=0, onClick=self.create_btn_click, image=pygame.transform.scale(create_Btn_img,(175,60)))
        
        solve_Btn_img:pygame.image = pygame.image.load("src/images/button_solve.png").convert()   
        self.solveBtn = Button(self.screen, self.screen_width-185, 285, 175, 60, radius=0, onClick=self.clear_grid, image=pygame.transform.scale(solve_Btn_img,(175,60)))
        
        clear_Btn_img:pygame.image = pygame.image.load("src/images/button_create.png").convert()   
        self.clearBtn = Button(self.screen, self.screen_width-370, 365, 175, 60, radius=0, onClick=self.clear_btn_click, image=pygame.transform.scale(clear_Btn_img,(175,60)))
        
        save_Btn_img:pygame.image = pygame.image.load("src/images/button_solve.png").convert()   
        self.saveBtn = Button(self.screen, self.screen_width-185, 365, 175, 60, radius=0, onClick=self.clear_grid, image=pygame.transform.scale(save_Btn_img,(175,60)))
        # Draw text in view
        self.draw_labels("Options", self.title_font,self.color_black,self.screen_width-248,455)
        
        # Design of the 4 secondary buttons whose objectives are to let the user choose which algorithm they want to solve the maze with
        # Each button is named after the function that can be used for resolution (L*, Breadth, Depth, A*)
        lsBtn:pygame.image = pygame.image.load("src/images/button_clear-maze.png").convert()  
        self.lsearchbtn:Button = Button(self.screen, self.screen_width-370, 508, 175, 60, radius=50, onClick=self.clear_grid, image=pygame.transform.scale(lsBtn,(175,60)))

        brBtn:pygame.image = pygame.image.load("src/images/button_breadth-algorithm.png").convert()  
        self.breadthBtn:Button = Button(self.screen, self.screen_width-185, 508, 175, 60, radius=50, onClick=self.clear_grid, image=pygame.transform.scale(brBtn,(175,60)))

        daBtn:pygame.image = pygame.image.load("src/images/button_depth-algorithm.png").convert()  
        self.depthBtn:Button = Button(self.screen, self.screen_width-370, 588, 175, 60, radius=50, onClick=self.clear_grid, image=pygame.transform.scale(daBtn,(175,60)))

        asBtn:pygame.image = pygame.image.load("src/images/button_a-search-algorithm.png").convert()  
        self.asearchBtn:Button = Button(self.screen, self.screen_width-185, 588, 175, 60, radius=50, onClick=self.clear_grid, image=pygame.transform.scale(asBtn,(175,60)))
        
        pygame.display.update()#updates the display
    
    # Method called when clicking on the walls picker_color button    
    def pick_color_btn_wls_click(self) -> None:
        self.current_color_wls:'pickerView' = self.pickerView.color_picker(self.current_color_wls,self)
        self.rect_wls:pygame.rect = pygame.draw.rect(self.screen, self.current_color_wls, (self.screen_width-57, 165, 35, 35))
        self.clear_grid()
    
    # Method called when clicking on the background picker_color button
    def pick_color_btn_bg_click(self) -> None:
        self.current_color_bg:'pickerView' = self.pickerView.color_picker(self.current_color_bg,self)
        self.rect_bg:pygame.rect = pygame.draw.rect(self.screen, self.current_color_bg, (self.screen_width-57, 215, 35, 35))
        self.clear_grid()

    # Metodo chamado quando se clica no botao principal create
    def create_btn_click(self) -> None:
        self.createBtn.disable()
        self.pick_color_btn_wls.disable()
        self.pick_color_btn_bg.disable()
        self.draw_maze()
    
    # Metodo chamado quando se clica no botao principal solve
    def solve_btn_click(self) -> None:
        pass
    
    # Metodo chamado quando se clica no botão principal clear
    def clear_btn_click(self) -> None:
        self.createBtn.enable()
        self.pick_color_btn_wls.enable()
        self.pick_color_btn_bg.enable()
        self.clear_grid()
    
    # Metodo chamada quando se clica no botão principal Save
    def save_btn_click(self) -> None:
        pass
    
    # Method called when clicking on the secondary button for the L* Search algorithm
    def lsearchbtn_click(self) -> None:
        pass
    
    # 
    def draw_cell(self,cell, bg_color, wl_color) -> None: #desenhar a grid
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
            
    def draw_maze(self) -> None:
        #verificação do tamanho das colunas e linhas
        self.clear_grid()
        
        self.maze = self.view_controller.generate_maze(int(self.txtNumbRowss.getText()),int(self.txtNumbCols.getText()))
        for row in self.maze.get_grid():
            for cell in row:
                self.draw_cell(cell,self.current_color_bg,self.current_color_wls)
        self.draw_cell(self.maze.get_start_cell(),"green",self.current_color_wls)
        self.draw_cell(self.maze.get_end_cell(),"red",self.current_color_wls)

        pygame.display.update()
        
    def draw_labels(self,text,font, color, x, y) -> None:
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface,(x,y))

    def clear_grid(self) -> None:
        self.screen.fill((255,255,255),pygame.Rect(0, 0, self.screen_width-370, self.screen_height))

    







import os
import random
import pygame
import pygame_gui.ui_manager
from typing import Union
from controllers.cell_controller import CellController
from controllers.maze_controller import MazeController
from controllers.picker_view_controller import PickerViewController
class ViewController:
    # ViewController class constructor
    def __init__(self) -> None:
        self.maze_controller:MazeController = MazeController() # Maze controller     
        self.cell_controller:CellController = CellController() # Cell controller  
    
    # Check input rows and columns
    def check_inputs(self,rows:str,columns:str,width:int,height:int):
        try:
            #valid min columns = left margin + 5 * cell_size  || valid min height = top margin + 5 * cell_size
            if int(columns) < 5 and int(rows) < 5:
                return ("Min columns:5","Min rows:5")
            else:
                #valid max columns = width - right elements - left and right margins  || valid max height = height - top margin - bottom margin
                return () if int(columns)<=(width - 370 - 40) // 20 and int(rows)<=(height - 20 - 80) // 20 else (f"Max Columns:{(width - 370 - 40) // 20}",f"Max rows:{(height - 20 - 80) // 20}")
        except ValueError:
            return ("Write only integers","Write only integers")
       
    # Method that returns the starting cell
    def get_start_cell(self) -> 'Cell':
        return self.maze_controller.get_start_cell()
        
    # Method that returns the ending cells
    def get_end_cells(self) -> list['Cell']:
        return self.maze_controller.get_end_cells()
    
    # Method that, in connection with the Cell class controller, returns the value of the "x" attribute of the same
    def get_x_cell(self,cell:'Cell') -> int:
        return self.cell_controller.get_x(cell)
    
    # Method that, in connection with the Cell class controller, returns the value of the "y" attribute of the same
    def get_y_cell(self,cell:'Cell') -> int:
        return self.cell_controller.get_y(cell)
    
    # Method that, in connection with the Cell class controller, returns the value of the "size" attribute of the same
    def get_size_cell(self,cell:'Cell') -> int:
        return self.cell_controller.get_size(cell)
    
    # Method that, in connection with the Cell class controller, returns one value of the "walls" attribute of the same
    def get_wall(self,cell:'Cell',direction:str) -> str:
        return self.cell_controller.get_wall(cell,direction)
    
    # Method that aims to call the function in the color_picker window controller that opens it
    def open_color_picker(self,screen:pygame.display,ui_manager:pygame_gui.ui_manager,current_color:pygame.color) -> pygame.color:
        self.picker_color_controller:PickerViewController = PickerViewController()
        return self.picker_color_controller.open_color_picker(screen,ui_manager,current_color)
    
    # Method that contacts the maze controller to tell it to generate the maze
    def generate_maze(self,rows:int,cols:int) -> list[list['Cell']]: 
        self.maze_controller.set_grid(rows,cols) # Method that creates the grid
        self.grid_maze:list[list['Cell']] = self.maze_controller.generate_maze() # Method that creates the maze in the grid created above
        return self.grid_maze
    
    # Method that allows you to save the current maze in png format
    def save_maze(self,screen:pygame.display) -> None:
        pygame.display.flip()
        # We create a surface that represents the area to capture
        size:tuple = self.maze_controller.get_px_size_maze() # Get the size of the maze with margins
        capture_surface:pygame.Surface = pygame.Surface(size)
        # Capture the screen area, excluding the button part
        capture_surface.blit(screen, (0, 0), pygame.Rect(0, 0, size[0], size[1]))
        # Get the path of the user's "Images" folder
        folder_images:str = os.path.join(os.path.expanduser('~'), 'Pictures')
        # Save the image of the captured area
        pygame.image.save(capture_surface,os.path.join(folder_images, self.maze_controller.get_save_name_maze()))
        # Wait for the image to be saved
        pygame.time.delay(500)
    
    # Method to obtain a different color from the background and walls of the maze
    def get_different_color(self,color1: pygame.Color, color2: pygame.Color, color3: pygame.Color, color4: pygame.Color) -> pygame.Color:
        while True:
            new_color:pygame.color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            # Check if the new color is sufficiently different from color1
            if all(abs(new_color[i] - color1[i]) > 50 for i in range(3)):
                # Check if the new color is sufficiently different from color2
                if all(abs(new_color[i] - color2[i]) > 50 for i in range(3)):
                    # Check if the new color is sufficiently different from color3
                    if all(abs(new_color[i] - color3[i]) > 50 for i in range(3)):
                        # Check if the new color is sufficiently different from color4
                        if all(abs(new_color[i] - color4[i]) > 50 for i in range(3)):
                            return new_color
            
    # Methods for the Breadth algorithm
    def first_fase_breadth(self) -> None:
        self.maze_controller.first_fase_breadth()
    
    def second_fase_breadth(self) -> Union['Cell',list,None]:
        return self.maze_controller.second_fase_breadth()
    
    # Methods for the Depth algorithm
    def first_fase_depth(self) -> None:
        self.maze_controller.first_fase_depth()
    
    def second_fase_depth(self) -> Union['Cell',list,None]:
        return self.maze_controller.second_fase_depth()
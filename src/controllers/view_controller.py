import os
import random
from typing import Union
import pygame
import pygame_gui.ui_manager
from controllers.maze_controller import MazeController
from controllers.picker_view_controller import PickerViewController
class ViewController:
    # ViewController class constructor
    def __init__(self) -> None:
        self.maze_controller:MazeController = MazeController() # Maze controller
    
    # Check input rows and columns
    def check_inputs(self,columns:int,rows:int,width:int,height:int):
        valid_width:int = (width - 370 - 40) // 20
        valid_height:int = (height - 20 - 80) // 20
        
        return () if columns<=valid_width and rows<=valid_height else (valid_width,valid_height)
        
    # Method that contacts the maze controller to tell it to generate the maze
    def generate_maze(self,rows:int,cols:int) -> 'Maze': 
        self.maze_controller.set_grid(rows,cols) # Method that creates the grid
        self.maze:'Maze' = self.maze_controller.generate_maze() # Method that creates the maze in the grid created above
        return self.maze
    
    # Method that aims to call the function in the color_picker window controller that opens it
    def open_color_picker(self,screen:pygame.display,ui_manager:pygame_gui.ui_manager,current_color:pygame.color) -> pygame.color:
        self.picker_color_controller:PickerViewController = PickerViewController()
        return self.picker_color_controller.open_color_picker(screen,ui_manager,current_color)
    
    # Method that allows you to save the current maze in png format
    def save_maze(self,screen:pygame.display) -> None:
        pygame.display.flip()
        # We create a surface that represents the area to capture
        size:tuple = self.maze_controller.get_px_size_maze() # Get the size of the maze with margins
        captura_surface:pygame.Surface = pygame.Surface(size)
        # Capture the screen area, excluding the button part
        captura_surface.blit(screen, (0, 0), pygame.Rect(0, 0, size[0], size[1]))
        # Get the path of the user's "Images" folder
        folder_images:str = os.path.join(os.path.expanduser('~'), 'Pictures')
        # Save the image of the captured area
        pygame.image.save(captura_surface,os.path.join(folder_images, self.maze_controller.get_save_name_maze()))
        # Wait for the image to be saved
        pygame.time.delay(500)
    
    # Method that has the objective of clearing the solution of the current maze.
    def clear_solution(self) -> None:
        self.maze_controller.clear_solution()
    
    #################################################################################################################################
    def get_different_color(self,color1: pygame.Color, color2: pygame.Color, color3: pygame.Color, color4: pygame.Color) -> pygame.Color:
        while True:
            new_color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            
            # Verifica se a nova cor é suficientemente diferente de color1
            if all(abs(new_color[i] - color1[i]) > 50 for i in range(3)):
                # Verifica se a nova cor é suficientemente diferente de color2
                if all(abs(new_color[i] - color2[i]) > 50 for i in range(3)):
                    # Verifica se a nova cor é suficientemente diferente de color3
                    if all(abs(new_color[i] - color3[i]) > 50 for i in range(3)):
                        # Verifica se a nova cor é suficientemente diferente de color4
                        if all(abs(new_color[i] - color4[i]) > 50 for i in range(3)):
                            return new_color
            
    # Metodos para o algoritmo Breadth
    def first_fase_algorithm(self) -> None:
        self.maze_controller.first_fase_breadth()
    
    def second_fase_breadth(self) -> Union['Cell',list]:
        return self.maze_controller.second_fase_breadth()
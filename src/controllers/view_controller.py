import os
import pygame
import pygame_gui.ui_manager
from controllers.maze_controller import MazeController
from controllers.picker_view_controller import PickerViewController
class ViewController:
    # ViewController class constructor
    def __init__(self) -> None:
        self.maze_controller:MazeController = MazeController() # Maze controller
        
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
    


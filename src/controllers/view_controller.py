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
    


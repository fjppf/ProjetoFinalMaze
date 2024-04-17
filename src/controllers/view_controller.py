import pygame
from controllers import maze_controller
from views import view
class ViewController:
    def __init__(self):
        self.maze_controller = maze_controller.maze_controller()
        self.view = view.view(self)

    def generate_maze(self,rows:int,cols:int):
        self.maze_controller.set_grid(rows,cols)
        self.maze = self.maze_controller.generate_maze()
        return self.maze
        
    def should_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
    
    def update_ui(self):
        self.view.update_ui()
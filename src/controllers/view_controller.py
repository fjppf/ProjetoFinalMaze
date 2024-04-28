from controllers.maze_controller import maze_controller
from views.view import view
class ViewController:
    # ViewController class constructor
    def __init__(self) -> None:
        self.maze_controller:maze_controller = maze_controller() # Maze controller
        self.view:view = view(self) # User Interface do utilizador

    # Method that contacts the maze controller to tell it to generate the maze
    def generate_maze(self,rows:int,cols:int) -> 'Maze': 
        self.maze_controller.set_grid(rows,cols) # Method that creates the grid
        self.maze:'Maze' = self.maze_controller.generate_maze() # Method that creates the maze in the grid created above
        return self.maze


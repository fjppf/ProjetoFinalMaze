from models.Maze import Maze
class MazeController:
    # Class constructor
    def __init__(self) -> None:
        self.maze:Maze = Maze()
    
    # Create the grid on where the maze will be created
    def set_grid(self,rows:int,cols:int) -> None:
        self.maze.set_rows(rows) # Defines the number of lines in the grid
        self.maze.set_cols(cols) # Defines the number of columns in the grid
        self.maze.set_grid(self.maze.generate_grid()) # Build the grid
    
    # Calls the maze object method that allows generating the maze over the previously created grid
    def generate_maze(self) -> Maze:
        return self.maze.generate_maze()
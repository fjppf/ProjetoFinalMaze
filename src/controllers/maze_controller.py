from models.Maze import Maze
import random
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
    
    # Returns the size (width, height) of the maze in pixels with a 20 pixel margin all around
    def get_px_size_maze(self) -> tuple:
        return (self.maze.get_cols()*20+40,self.maze.get_rows()*20+40)
    
    # Get a valid name to save the maze
    def get_save_name_maze(self) -> str:
        return f"Maze {self.maze.get_cols()}x{self.maze.get_rows()}_{random.randint(0, 1000)}.png"
    
    # Clear the solution of the maze
    def clear_solution(self):
        self.maze.set_solution(None)
        
    #############################################################
    def first_fase_breadth(self) -> None:
        self.maze.first_fase_breadth()
    
    def second_fase_breadth(self):
        pass
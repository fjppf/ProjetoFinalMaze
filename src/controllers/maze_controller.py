from models import Maze

class maze_controller:
    def __init__(self):
        self.maze = Maze.Maze()
    
    def set_grid(self,rows,cols):
        self.maze.set_rows(rows)
        self.maze.set_cols(cols)
        self.maze.set_grid(self.maze.generate_grid())
        
    def generate_maze(self):
        return self.maze.generate_maze()
        
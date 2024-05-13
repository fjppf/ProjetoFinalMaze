import random
from typing import Union
from random import choice
from controllers.cell_controller import CellController
from models.Maze import Maze

class MazeController:
    # Class constructor
    def __init__(self) -> None:
        self.cell_controller:CellController = CellController()
        self.maze:Maze = Maze()
    
    # Method that generates the maze grid
    def generate_grid(self) -> list[list]:
        grid:list[list] = []
        # Cycle that will generate the matrix needed for the maze
        # We start the cycle at 1 so that the amtrix is ​​drawn with clearance from the edge of the window
        for row in range(1,self.maze.get_rows()+1):
            grid_row:list = []
            for col in range(1,self.maze.get_cols()+1):
                cell:'Cell' = self.cell_controller.create_cell(col,row)
                grid_row.append(cell)
            grid.append(grid_row)
        return grid
    
    # Create the grid on where the maze will be created
    def set_grid(self,rows:int,cols:int) -> None:
        self.maze.set_rows(rows) # Defines the number of lines in the grid
        self.maze.set_cols(cols) # Defines the number of columns in the grid
        self.maze.set_grid(self.generate_grid()) # Build the grid
    
    # Method that returns the starting cell
    def get_start_cell(self) -> 'Cell':
        return self.maze.get_start_cell()
    
    # Method that returns the ending cells
    def get_end_cells(self) -> list['Cell']:
        return self.maze.get_end_cells()
    
    # Method that see which square is currently in and returns the same
    def check_cell(self, x:int, y:int) -> Union['Cell',None]:
        for row in self.maze.get_grid():
            for cell in row:
                if self.cell_controller.get_x(cell) == x and self.cell_controller.get_y(cell) == y: return cell
        return None
    
    # Method that sees which neighbors are available and chooses one to follow
    def check_neighbors_generate_maze(self,cell:'Cell') -> 'Cell':
        neighbors:list = []
        # Check the top neighbor
        top:'Cell' = self.check_cell(self.cell_controller.get_x(cell), self.cell_controller.get_y(cell) - 1)
        # Check the right neighbor
        right:'Cell' = self.check_cell(self.cell_controller.get_x(cell) + 1, self.cell_controller.get_y(cell))
        # Check the bottom neighbor
        bottom:'Cell' = self.check_cell(self.cell_controller.get_x(cell), self.cell_controller.get_y(cell) + 1)
        # Check the left neighbor
        left:'Cell' = self.check_cell(self.cell_controller.get_x(cell) - 1, self.cell_controller.get_y(cell))

        # If there is a cell on top/right/bottom/left of the current cell, and that cell(top/right/bottom/left) it's not visited 
        # gets added to the list.
        if top and not self.cell_controller.get_visited(top):
            neighbors.append(top)
        if right and not self.cell_controller.get_visited(right):
            neighbors.append(right)
        if bottom and not self.cell_controller.get_visited(bottom): 
            neighbors.append(bottom)
        if left and not self.cell_controller.get_visited(left): 
            neighbors.append(left)
        return neighbors
    
    # Method to clear all visited houses in the maze
    def clear_visited_attribute(self) -> None:
        # Clear all visited attributes of each maze cell for future use in the search for resolution
        temp_grid:list[list] = self.maze.get_grid()[:] # Temporary variable to store the current grid
        for row in range(0,self.maze.get_rows()):            
            for col in range(0,self.maze.get_cols()):
                self.cell_controller.set_visited(temp_grid[row][col],False)
        self.maze.set_grid(temp_grid)
        del temp_grid # Free memory by deleting temporary variable
        
    # Method that will generate the maze itself 
    def generate_maze(self) -> 'Maze':
        self.maze.set_end_cells([])
        self.maze.set_current_cell(self.maze.get_grid()[0][0])
        # Loop until there are no more unvisited cells
        while True: 
            self.cell_controller.set_visited(self.maze.get_current_cell(),True) # Mark the current cell as visited
            self.cell_controller.set_neighbors(self.maze.get_current_cell(),self.check_neighbors_generate_maze(self.maze.get_current_cell())) # Assigns its neighbors to the cell
            # Get the next unvisited neighbor. If there is more than one we choose randomly
            self.maze.set_next_cell(choice(self.cell_controller.get_neighbors(self.maze.get_current_cell()))) if self.cell_controller.get_neighbors(self.maze.get_current_cell()) else self.maze.set_next_cell(None)
            if self.maze.get_next_cell(): # If there is an unvisited neighbor
                self.cell_controller.set_visited(self.maze.get_next_cell(),True) # Mark the next cell as visited
                self.maze.add_stack(self.maze.get_current_cell()) # Add the current cell to the stack
                self.cell_controller.remove_walls(self.maze.get_current_cell(),self.maze.get_next_cell()) # Remove the walls between the current and next cell
                self.maze.set_current_cell(self.maze.get_next_cell())  # Move to the next cell
            elif self.maze.get_stack(): # If the stack is not empty
                self.maze.set_current_cell(self.maze.remove_stack()) # Move back to the previous cell
            else:
                break # Exit the loop when there are no more unvisited cells
            
        # Assign a random starting house in the 1st quadrant of the maze
        self.maze.set_start_cell(self.maze.get_grid()[random.randint(0, self.maze.get_rows()//2)][random.randint(0,self.maze.get_cols()//2)])

        # Assign the final cells to the maze
        self.maze.set_final_cells()
        
        # Clear all visited attributes of each maze cell for future use in the search for resolution
        self.clear_visited_attribute()
        
        # Clear all variables used
        self.cell_controller.set_neighbors(self.maze.get_current_cell(),None)
        self.maze.set_current_cell(None)
        self.maze.set_stack([])
        self.maze.set_next_cell(None)
        
        return self.maze.get_grid()
    
    # Method that establishes the connections between the cell controller and maze controller in order to invoke the method in the cell controller to create a new cell.
    def create_cell(self,x:int,y:int) -> 'Cell':
        return self.cell_controller.create_cell(x,y)
    
    # Returns the size (width, height) of the maze in pixels with a 20 pixel margin all around
    def get_px_size_maze(self) -> tuple:
        return (self.maze.get_cols()*20+40,self.maze.get_rows()*20+40)
    
    # Get a valid name to save the maze
    def get_save_name_maze(self) -> str:
        return f"Maze {self.maze.get_cols()}x{self.maze.get_rows()}_{random.randint(0, 1000)}.png"
        
    # Method that starts the Breadth Search algorithm
    def first_fase_breadth(self) -> None:
        self.maze.set_solutions([]) # Clear the solutions variable
        self.maze.add_queue(self.get_start_cell()) # add the initial cell to the queue
        self.maze.add_paths([self.get_start_cell()]) # add to path list
    
    # Method that will explore the entire maze trying to find all the paths from the beginning to the destination, destinations or void
    def second_fase_breadth(self) -> Union['Cell',None,list]:
        self.maze.set_current_cell(self.maze.remove_queue())
        self.cell_controller.set_visited(self.maze.get_current_cell(),True) # Mark the current cell as visited
        # We get all the neighbors that have not yet been visited of the current cell
        self.cell_controller.set_neighbors(self.maze.get_current_cell(),self.check_neighbors_breadth_algorithm(self.maze.get_current_cell()))
        #This piece of code creates all possible paths from the current cell in the maze. If more than one neighbor is available, we add the first neighbor to the existing path. 
        # For subsequent neighbors, we copy the current path, excluding the last element (which is already the current neighbor), and add the neighbor under consideration. 
        # This process is repeated for each neighbor, ensuring that we explore all path options from the current cell.        
        for neighbor_cell in self.cell_controller.get_neighbors(self.maze.get_current_cell()):
            if neighbor_cell == self.cell_controller.get_neighbors(self.maze.get_current_cell())[0]: 
                self.maze.add_element_path(self.maze.get_current_cell(), neighbor_cell)
            else:
                self.maze.add_copy_path(self.maze.get_current_cell(), neighbor_cell)
            self.maze.add_queue(neighbor_cell)
                               
        # If the queue still has elements we need to do some checks
        if len(self.maze.get_queue()) != 0:
            # If the next cell is the final one then we save this path as a solution
            if self.maze.get_queue()[0] in self.maze.get_end_cells():
                self.maze.save_solution()
                # If all the necessary solutions have already been found, then we return these
                if len(self.maze.get_solutions()) == len(self.maze.get_end_cells()):
                    self.clear_visited_attribute() # Clear all visited attributes
                    self.maze.clear_breadth_variables()
                    return self.maze.get_solutions()
                return None
            # we return the next one to be seen
            else:
                return self.maze.get_queue()[0]
        # If the queue is empty then all the houses have already been explored, we return all the paths found so far
        else:
            self.clear_visited_attribute() # Clear all visited attributes
            self.cell_controller.set_neighbors(self.maze.get_current_cell(),None)
            self.maze.clear_breadth_variables() # Clear all variables used
            return self.maze.get_solutions()  # return solutions
    
    # Method that sees which neighbors are available and chooses one to follow
    def check_neighbors_breadth_algorithm(self,cell:'Cell') -> 'Cell':
        neighbors:list['Cell'] = []
        # Check the top neighbor
        top:'Cell' = self.check_cell(self.cell_controller.get_x(cell), self.cell_controller.get_y(cell)-1)
        # Check the right neighbor
        right:'Cell' = self.check_cell(self.cell_controller.get_x(cell) + 1, self.cell_controller.get_y(cell))
        # Check the bottom neighbor
        bottom:'Cell' = self.check_cell(self.cell_controller.get_x(cell), self.cell_controller.get_y(cell) + 1)
        # Check the left neighbor
        left:'Cell' = self.check_cell(self.cell_controller.get_x(cell) - 1, self.cell_controller.get_y(cell))

        # If there is a cell on top/right/bottom/left of the current cell, and that cell(top/right/bottom/left) it's not visited 
        # gets added to the list.
        if top and not self.cell_controller.get_visited(top) and not self.cell_controller.get_wall(top,"bottom"):
            neighbors.append(top)
        if right and not self.cell_controller.get_visited(right) and not self.cell_controller.get_wall(right,"left"):
            neighbors.append(right)
        if bottom and not self.cell_controller.get_visited(bottom) and not self.cell_controller.get_wall(bottom,"top"): 
            neighbors.append(bottom)
        if left and not self.cell_controller.get_visited(left) and not self.cell_controller.get_wall(left,"right"): 
            neighbors.append(left)
        return neighbors
    
    def first_fase_depth(self) -> None:
        self.maze.set_solutions([]) # Clear the solutions variable
        self.maze.set_current_cell(self.maze.get_grid()[0][0])
    
    def second_fase_depth(self):
        self.cell_controller.set_visited(self.maze.get_current_cell(),True) # Mark the current cell as visited
        self.cell_controller.set_neighbors(self.maze.get_current_cell(),self.check_neighbors_generate_maze(self.maze.get_current_cell())) # Assigns its neighbors to the cell
        # Get the next unvisited neighbor. If there is more than one we choose randomly
        self.maze.set_next_cell(choice(self.cell_controller.get_neighbors(self.maze.get_current_cell()))) if self.cell_controller.get_neighbors(self.maze.get_current_cell()) else self.maze.set_next_cell(None)
        if self.maze.get_next_cell(): # If there is an unvisited neighbor
            self.cell_controller.set_visited(self.maze.get_next_cell(),True) # Mark the next cell as visited
            self.maze.add_stack(self.maze.get_current_cell()) # Add the current cell to the stack
            self.maze.add_element_path(self.maze.get_current_cell(), self.maze.get_next_cell())
            self.maze.set_current_cell(self.maze.get_next_cell())  # Move to the next cell
        elif self.maze.get_stack(): # If the stack is not empty
            self.maze.set_current_cell(self.maze.remove_stack()) # Move back to the previous cell
            self.maze.set_paths(self.maze.get_paths()[0][0:self.maze.get_paths()[0].index(self.maze.get_current_cell())])
        else:
            return self.maze.get_solutions()
        
        if self.maze.get_next_cell() in self.maze.get_end_cells():
            pass
            return None
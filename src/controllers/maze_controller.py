import math
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
    
    # Method that establishes the connections between the cell controller and maze controller in order to invoke the method in the cell controller to create a new cell.
    def create_cell(self,x:int,y:int) -> 'Cell':
        return self.cell_controller.create_cell(x,y)
    
    # Returns the size (width, height) of the maze in pixels with a 20 pixel margin all around
    def get_px_size_maze(self) -> tuple:
        return (self.maze.get_cols() * 20 + 40,self.maze.get_rows() * 20 + 40)
    
    # Get a valid name to save the maze
    def get_save_name_maze(self) -> str:
        return f"Maze {self.maze.get_cols()}x{self.maze.get_rows()}_{random.randint(0, 1000)}.png"
    
    # Method that see which cell we are currently in and returns the same
    def check_cell(self, x:int, y:int) -> Union['Cell',None]:
        for row in self.maze.get_grid():
            for cell in row:
                if self.cell_controller.get_x(cell) == x and self.cell_controller.get_y(cell) == y: return cell
        return None
    
    # Method that generates the maze grid
    def generate_grid(self) -> list[list['Cell']]:
        grid:list[list['Cell']] = []
        # Cycle that will generate the matrix needed for the maze
        # We start the cycle at 1 so that the amtrix is ​​drawn with clearance from the edge of the window
        for row in range(1,self.maze.get_rows()+1):
            grid_row:list = []
            for col in range(1,self.maze.get_cols()+1):
                cell:'Cell' = self.cell_controller.create_cell(col,row)
                grid_row.append(cell)
            grid.append(grid_row)
        return grid
    
    # Method that find the neighbors if they exist around the cell
    def find_neighbors(self,cell:'Cell') -> list['Cell']:
        # Check the top neighbor
        top:'Cell' = self.check_cell(self.cell_controller.get_x(cell), self.cell_controller.get_y(cell)-1)
        # Check the right neighbor
        right:'Cell' = self.check_cell(self.cell_controller.get_x(cell) + 1, self.cell_controller.get_y(cell))
        # Check the bottom neighbor
        bottom:'Cell' = self.check_cell(self.cell_controller.get_x(cell), self.cell_controller.get_y(cell) + 1)
        # Check the left neighbor
        left:'Cell' = self.check_cell(self.cell_controller.get_x(cell) - 1, self.cell_controller.get_y(cell))
        return (top,right,bottom,left)
        
    # Method that sees which neighbors are available and chooses one to follow
    def check_neighbors_generate_maze(self,cell:'Cell') -> list['Cell']:
        neighbors:list['Cell'] = []
        # Neighbors
        top,right,bottom,left = self.find_neighbors(cell)

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
        
    # Method that will generate the maze itself 
    def generate_maze(self) -> 'Maze':
        self.maze.set_end_cells([])
        self.maze.set_current_cell(self.maze.get_grid()[0][0])
        # Loop until there are no more unvisited cells
        while True: 
            current_cell:'Cell' = self.maze.get_current_cell()
            self.cell_controller.set_visited(current_cell,True) # Mark the current cell as visited
            neighbors:list['Cell'] = self.check_neighbors_generate_maze(current_cell) # Get the neighbors of the cell
            
            next_cell:'cell' = choice(neighbors) if neighbors else None
            if next_cell: # If there is an unvisited neighbor
                self.maze.add_stack(current_cell) # Add the current cell to the stack
                self.cell_controller.remove_walls(current_cell,next_cell) # Remove the walls between the current and next cell
                self.maze.set_current_cell(next_cell)  # Move to the next cell
            elif self.maze.get_stack(): # If the stack is not empty
                self.maze.set_current_cell(self.maze.pop_stack()) # Move back to the previous cell
            else:
                break # Exit the loop when there are no more unvisited cells
            
        # Assign a random starting house in the 1st quadrant of the maze -> grid()[0-(num_linhas/2)][0-num_cols/2]
        self.maze.set_start_cell(self.maze.get_grid()[random.randint(0, self.maze.get_rows()//2)][random.randint(0,self.maze.get_cols()//2)])
        # Assign the final cells to the maze
        self.maze.set_final_cells()
        # Clear all visited attributes of each maze cell for future use in the search for resolution
        self.clear_visited_attribute()
        # Clear all variables used
        self.maze.set_current_cell(None)
        self.maze.set_stack([])
        return self.maze.get_grid()
    
    
    # Method that sees which neighbors are available and chooses one to follow
    def check_neighbors_algorithms(self,cell:'Cell') -> list['Cell']:
        neighbors:list['Cell'] = []
        top,right,bottom,left = self.find_neighbors(cell) # Neighbors
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
      
        
    # Method that starts the Breadth Search algorithm
    def first_fase_breadth(self) -> None:
        self.maze.set_solutions([]) # Clear the solutions variable
        start_cell:'Cell' = self.get_start_cell()
        self.maze.add_queue(start_cell) # Add the initial cell to the queue
        self.maze.add_paths([start_cell]) # Add to path list
    
    # Method that will explore the entire maze trying to find all the paths from the beginning to the destination, destinations or void
    def second_fase_breadth(self) -> Union['Cell',None,list]:
        current_cell:'Cell' = self.maze.remove_queue()
        self.maze.set_current_cell(current_cell)
        self.cell_controller.set_visited(current_cell,True) # Mark the current cell as visited
        
        # We get all the neighbors that have not yet been visited of the current cell
        neighbors:list['Cell'] = self.check_neighbors_algorithms(current_cell)
        
        # This piece of code creates all possible paths from the current cell in the maze. If more than one neighbor is available, we add the first neighbor to the existing path. 
        # For subsequent neighbors, we copy the current path, excluding the last element (which is already the current neighbor), and add the neighbor under consideration. 
        # This process is repeated for each neighbor, ensuring that we explore all path options from the current cell.        
        for neighbor_cell in neighbors:
            if neighbor_cell == neighbors[0]: 
                self.maze.add_element_path(current_cell, neighbor_cell)
            else:
                self.maze.add_copy_path(current_cell, neighbor_cell)
            self.maze.add_queue(neighbor_cell)
                               
        # If the queue still has elements we need to do some checks
        if self.maze.get_queue():
            # If the next cell is the final one then we save this path as a solution
            next_cell:'Cell' = self.maze.get_queue()[0]
            if  next_cell in self.maze.get_end_cells():
                self.maze.save_solution()
                # If all the necessary solutions have already been found, then we return these
                if len(self.maze.get_solutions()) == len(self.maze.get_end_cells()):
                    self.clear_visited_attribute() # Clear all visited attributes
                    self.maze.clear_breadth_variables()
                    return self.maze.get_solutions()
                return None
            # we return the next one to be seen
            else:
                return next_cell
        # If the queue is empty then all the houses have already been explored, we return all the paths found so far
        else:
            self.clear_visited_attribute() # Clear all visited attributes
            self.maze.clear_breadth_variables() # Clear all variables used
            return self.maze.get_solutions()  # return solutions
    
    # Method that clean the variables used in the respective algorithm
    def delete_breadth(self) -> None:
        self.maze.clear_breadth_variables()
        self.clear_visited_attribute()
    
    
    # Method that starts the Depth Search algorithm
    def first_fase_depth(self) -> None:
        self.maze.set_solutions([]) # Clear the solutions variable
        start_cell:'Cell' = self.get_start_cell()
        self.maze.set_current_cell(start_cell)
        self.maze.add_paths([start_cell]) # add to path list
    
    def second_fase_depth(self) -> Union['Cell',None,list]:
        current_cell:'Cell' = self.maze.get_current_cell()
        self.cell_controller.set_visited(current_cell,True) # Mark the current cell as visited
        neighbors:list['Cell'] = self.check_neighbors_algorithms(current_cell)
        
        # Get the next unvisited neighbor. If there is more than one we choose randomly
        next_cell:'Cell' = choice(neighbors) if neighbors else None
        if next_cell: # If there is an unvisited neighbor
            self.maze.add_stack(current_cell) # Add the current cell to the stack
            self.maze.add_element_path(current_cell, next_cell)
            self.maze.set_current_cell(next_cell)  # Move to the next cell
        elif self.maze.get_stack(): # If the stack is not empty
            self.maze.set_current_cell(self.maze.pop_stack()) # Move back to the previous cell
            self.maze.set_paths([self.maze.get_paths()[0][0:self.maze.get_paths()[0].index(self.maze.get_current_cell())+1]])
            return None
        else:
            self.clear_visited_attribute() # Clear all visited attributes
            self.maze.clear_depth_A_variables()
            return self.maze.get_solutions()
        
        current_cell = self.maze.get_current_cell()
        end_cells:list['Cell'] = self.maze.get_end_cells()
        if current_cell in end_cells:
            self.maze.save_solution()
            # If all the necessary solutions have already been found, then we return these
            if len(self.maze.get_solutions()) == len(end_cells):
                self.clear_visited_attribute() # Clear all visited attributes
                self.maze.clear_depth_A_variables()
                return self.maze.get_solutions()
            return None
        else:
            return current_cell
    
    # Method that clean the variables used in the Depth and A* algorithms  
    def delete_depth_A(self) -> None:
        self.clear_visited_attribute()
        self.maze.clear_depth_A_variables()
    
    # Method that starts the A* Search algorithm
    def first_fase_A(self) -> None:
        self.maze.set_solutions([]) # Clear the solutions variable
        start_cell:'Cell' = self.maze.get_start_cell()
        self.maze.set_current_cell(start_cell)
        self.maze.add_paths([start_cell]) # Add to path list
        self.maze.add_stack(start_cell) # Add to the stack

    def second_fase_A(self) -> Union['Cell',None,list]:
        # As this algorithm assumes that we know the final places, we can immediately check whether or not there are final places, 
        # if they do not exist, the list of possible paths will be returned to 0.
        if len(self.maze.get_end_cells())==0:
            return self.maze.get_solutions()
        
        current_cell:'Cell' = self.maze.get_current_cell()
        self.cell_controller.set_visited(current_cell,True) # Mark the current cell as visited
        neighbors:list['Cell'] = self.check_neighbors_algorithms(current_cell) # Get the neighbors of the cell

        # Add the neighbors to the stack and remove the current one from it
        for neighbor in neighbors:
            self.maze.add_stack(neighbor)
        self.maze.remove_stack(current_cell)
        
        # We get the next_cell using the "choose_best_cell" method
        next_cell:'Cell' = self.choose_best_cell(self.maze.get_stack(),len(self.maze.get_solutions())) 
        
        if next_cell: # If exists the next cell
            for neighbor_cell in neighbors:
                if neighbor_cell == neighbors[0]: 
                    self.maze.add_element_path(current_cell, neighbor_cell)
                else:
                    self.maze.add_copy_path(current_cell, neighbor_cell)
            self.maze.set_current_cell(next_cell)  
        else: # Ends the algorithm
            self.clear_visited_attribute() 
            self.maze.clear_depth_A_variables() 
            return self.maze.get_solutions()
        
        # Final verification to save the solution if necessary
        end_cells:list['Cell'] = self.maze.get_end_cells()
        if next_cell in end_cells:
            self.maze.save_solution()
            # If all the necessary solutions have already been found, then we return these
            if len(self.maze.get_solutions()) == len(end_cells):
                self.clear_visited_attribute() 
                self.maze.clear_depth_A_variables()
                return self.maze.get_solutions()
            return None
        else:
            return next_cell
    
    # Method that will determine which previously visited cell has the lowest cost among the initial cell, the currently evaluated cell, and the final cell in order to obtain the best cell
    def choose_best_cell(self,cells:list['Cell'],index:int)->'Cell':
        optimal_cell:'Cell' = None
        # We start the distance variable as high as possible
        min_distance:float = float('inf')
        # Get the coordinates of the final cell
        end_cell_coords:int = (self.cell_controller.get_x(self.maze.get_end_cells()[index]) + 10,
                        self.cell_controller.get_y(self.maze.get_end_cells()[index]) + 10)
            
        for cell in cells:
            # # Distance between the starting cell and the cell -> g(n)
            # distance_start:int = math.sqrt(((self.cell_controller.get_x(self.maze.get_start_cell())+10)-(self.cell_controller.get_x(cell)+10))**2 + ((self.cell_controller.get_y(self.maze.get_start_cell())+10)-(self.cell_controller.get_y(cell)+10))**2) 
            # # Distance between the cell and one of the ending cells -> h(n)
            # distance_end:int = math.sqrt(((self.cell_controller.get_x(cell)+10)-(self.cell_controller.get_x(self.maze.get_end_cells()[index])+10))**2 + ((self.cell_controller.get_y(cell)+10)-(self.cell_controller.get_y(self.maze.get_end_cells()[index])+10))**2)
            # # Total cost -> f(n)  =g(n) + h(n)
            # total_distance:int = distance_start + distance_end
            
            # Get current cell coordinates
            current_cell_coords = (self.cell_controller.get_x(cell) + 10,
                                self.cell_controller.get_y(cell) + 10)
            # distance = distance between the final_cell and the checked cell
            distance = math.sqrt((current_cell_coords[0] - end_cell_coords[0]) ** 2 +
                                (current_cell_coords[1] - end_cell_coords[1]) ** 2)
            
            # Check what is the minor total cost and save that value for future check, and save that cell
            if distance < min_distance:
                min_distance = distance
                optimal_cell = cell    
        return optimal_cell
    


        
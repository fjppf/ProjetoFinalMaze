from models.Cell import Cell

class CellController:
    # Constructor of the CellController class
    def __init__(self) -> None:
        pass
        
    # Method that allows the creation of a new cell
    def create_cell(self,x:int,y:int) -> Cell:
        return Cell(x,y)
    
    # Method that returns the value of the x attribute of the cell passed as a parameter
    def get_x(self,cell:Cell) -> int:
        return cell.get_x()
    
    # Method that returns the value of the y attribute of the cell passed as a parameter
    def get_y(self,cell:Cell) -> int:
        return cell.get_y()
    
    # Method that returns the value of the size attribute of the cell passed as a parameter
    def get_size(self,cell:Cell) -> int:
        return cell.get_size()
    
    # Method that returns a value of the walls attribute of the cell passed as a parameter
    def get_wall(self,cell:Cell,direction:str) -> str:
        return cell.get_wall(direction)
    
    # Method that makes use of the method named "remove_walls" of the Cell class, which aims to remove certain stops by checking the current cell and the next
    def remove_walls(self,cell:Cell, next:'Cell') -> None:
        cell.remove_walls(next)
        
    # Methods that make use of the get and set methods of the visited attribute of the passed cell
    def get_visited(self,cell:Cell) -> bool:
        return cell.get_visited()   
    def set_visited(self,cell:Cell,visited:bool) -> None:
        cell.set_visited(visited)
        
    # Methods that make use of the get and set methods of the neighbors attribute of the passed cell
    def get_neighbors(self,cell:Cell)->list:
        return cell.get_neighbors()
    def set_neighbors(self,cell:Cell,list:list)->None:
        cell.set_neighbors(list)
    
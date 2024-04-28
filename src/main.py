# To run this code it is necessary to install some libraries before running so use the command 
# "pip install -r requirements.txt"

import pygame
from controllers.controller_manager import ControllerManager
from controllers.view_controller import ViewController

def main() -> None:
    pygame.init()
    # Creating the view controller instance
    view_controller:ViewController = ViewController()
    # creating the manager controller instance
    manager:ControllerManager = ControllerManager()
    # Add the controllers we want it to run to the controller manager
    manager.add_controller(view_controller)
    # Run the method called "run" from controller_manager which will make it the main function of the program
    manager.run()


if __name__ == "__main__":
    main()
    
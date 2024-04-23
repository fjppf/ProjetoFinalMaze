# To run this code it is necessary to install some libraries before running so use the command 
# "pip install -r requirements.txt"

import pygame
from controllers import controller_manager,view_controller

def main():
    pygame.init()
    # Creating the view controller instance
    viewController:view_controller = view_controller.ViewController()
    # creating the manager controller instance
    manager:controller_manager = controller_manager.ControllerManager()
    # Add the controllers we want it to run to the controller manager
    manager.add_controller(viewController)
    # Run the method called "run" from controller_manager which will make it the main function of the program
    manager.run()


if __name__ == "__main__":
    main()
    
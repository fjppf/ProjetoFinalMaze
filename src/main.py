#It is necessary to install some libraries before running so use the command 
# "pip install -r requirements.txt"

import pygame
from controllers import controller_manager,view_controller

def main():
    pygame.init()
    viewController = view_controller.ViewController()
    manager = controller_manager.ControllerManager()
    manager.add_controller(viewController)
    manager.run()


if __name__ == "__main__":
    main()
    
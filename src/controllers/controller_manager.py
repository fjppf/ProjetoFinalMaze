import pygame
import pygame_widgets
class ControllerManager:
    # Class constructor
    def __init__(self) -> None:
        # List of controllers that we will manage
        self.controllers:list = []
        # Pygame library object to monitor frame rate and manage simulator event timings
        self.clock:pygame.time = pygame.time.Clock()
        # Limits refresh rate to 300 times per second
        self.clock.tick(300)

    # Method to add to controller list
    def add_controller(self, controller) -> None:
        self.controllers.append(controller)

    # Main function that will manage the entire program
    def run(self) -> None:
        running:bool = True
        while running:  
            events:pygame.event = pygame.event.get()  # Get all events
            for event in events:
                if event.type == pygame.QUIT: # User clicks the window close button
                    running = False
                    break  
                
            pygame_widgets.update(events) # Update Pygame widgets
            pygame.display.flip() # Update the screen once per iteration
            
        pygame.quit() # Closes the program and all processes
            



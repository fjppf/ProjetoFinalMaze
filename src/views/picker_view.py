import pygame
import pygame_gui
from pygame_gui.windows import UIColourPickerDialog

class PickerView:
    # Class constructor
    def __init__(self,screen:pygame.display,ui_manager:pygame_gui.UIManager) -> None:
        self.screen: pygame.display = screen
        self.ui_manager:pygame_gui.UIManager = ui_manager
    
    # Method that opens the dialog window that allows the user to choose the desired color
    def color_picker(self, current_colour:pygame.Color) -> pygame.Color:
        colour_picker:UIColourPickerDialog = UIColourPickerDialog(pygame.Rect(160, 50, 420, 400), self.ui_manager, window_title="Pick color", initial_colour=current_colour)
        colour_picker.show() # Show the colorpicker
        run:bool = True
        # While the window is open we check all events that exist in that window
        while run:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if colour_picker.ok_button.rect.collidepoint(event.pos):  # Clicked on the OK button
                        run = False
                    elif colour_picker.cancel_button.rect.collidepoint(event.pos):  # Clicked on the cancel button
                        run = False
                    elif colour_picker.close_window_button.rect.collidepoint(event.pos): # Clicked the close button
                        run = False       
                self.ui_manager.process_events(event)
            self.ui_manager.update(0)  # Update the graphical interface
            self.ui_manager.draw_ui(self.screen)  # Draw graphical interface elements on the screen
            pygame.display.flip()  # Refresh the screen
        colour_picker.kill() # Close the window
        return colour_picker.get_colour() # Returns the color chosen by the user
    
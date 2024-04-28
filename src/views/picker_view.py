from pygame_gui.windows import UIColourPickerDialog
import pygame
import pygame_gui

class picker_view:
    
    def __init__(self,screen,ui_manager) -> None:
        self.screen = screen
        self.ui_manager = ui_manager
    
    def color_picker(self, current_colour):
        colour_picker = UIColourPickerDialog(pygame.Rect(160, 50, 420, 400), self.ui_manager, window_title="Pick color", initial_colour=current_colour)
        colour_picker.show()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if colour_picker.ok_button.rect.collidepoint(event.pos):  # Clicou no botão OK
                        run = False
                    elif colour_picker.cancel_button.rect.collidepoint(event.pos):  # Clicou no botão de cancelar
                        run = False
                    elif colour_picker.close_window_button.rect.collidepoint(event.pos):
                        run = False       
                self.ui_manager.process_events(event)

            self.ui_manager.update(0)  # Atualizar a interface gráfica
            self.ui_manager.draw_ui(self.screen)  # Desenhar elementos da interface gráfica na tela
            pygame.display.flip()  # Atualizar a tela
            
        colour_picker.kill()
        return colour_picker.get_colour()
    
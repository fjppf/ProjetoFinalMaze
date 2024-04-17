import pygame
import pygame_widgets
class ControllerManager:
    def __init__(self):
        self.controllers = []
        self.clock = pygame.time.Clock()

    def add_controller(self, controller):
        self.controllers.append(controller)

    def run(self):
        # Limita a taxa de atualização para 200 vezes por segundo
        self.clock.tick(300)
        running = True
        while running:  
            events = pygame.event.get()  # Obtém todos os eventos
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                    break  # Sair do loop se for para fechar a janela
            
            # Atualiza a interface do usuário para todos os controladores
            for controller in self.controllers:
                controller.update_ui()
                
            # Atualiza os widgets do Pygame
            pygame_widgets.update(events)
            
            # Atualiza a tela uma vez por iteração
            pygame.display.update()
            
            
            
        pygame.quit()
            



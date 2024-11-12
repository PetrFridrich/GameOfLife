import pygame

from pygame.locals import *
from game_of_life import GameOfLife


class ButtonManager:

    def __init__(self, screen_width, banner_y):

        # Load images and initialize buttons
        self.images = {
            "play": pygame.image.load('./images/play.png'),
            "pause": pygame.image.load('./images/pause.png'),
            "reset": pygame.image.load('./images/refresh.png'),
            "slow_down": pygame.image.load('./images/slower.png'),
            "speed_up": pygame.image.load('./images/faster.png'),
        }

        button_width = 30
        button_height = 30
        spacing = 20
        total_button_width = 5 * button_width + 4 * spacing
        start_x = (screen_width - total_button_width) // 2
        
        # Button rects with labels
        self.buttons = {
            "slow_down": pygame.Rect(start_x, banner_y + 10, button_width, button_height),
            "play": pygame.Rect(start_x + (button_width + spacing), banner_y + 10, button_width, button_height),
            "pause": pygame.Rect(start_x + 2 * (button_width + spacing), banner_y + 10, button_width, button_height),
            "reset": pygame.Rect(start_x + 3 * (button_width + spacing), banner_y + 10, button_width, button_height),
            "speed_up": pygame.Rect(start_x + 4 * (button_width + spacing), banner_y + 10, button_width, button_height),
        }

        # Resize images to fit button dimensions
        for name, image in self.images.items():
            self.images[name] = pygame.transform.scale(image, (button_width, button_height))


    def draw(self, screen):

        # Draw buttons with images
        for name, rect in self.buttons.items():
            screen.blit(self.images[name], rect.topleft)


    def get_clicked_button(self, pos):

        # Check if any button is clicked and return its name
        for name, rect in self.buttons.items():
            if rect.collidepoint(pos):
                return name
        return None


class GameWindow:

    def __init__(self, cell_size=5, grid_size=(100, 100)):

        self.cell_size = cell_size
        self.grid_size = grid_size
        self.banner_height = 50
        self.width = grid_size[1] * cell_size
        self.height = grid_size[0] * cell_size + self.banner_height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")

        # Colors
        self.dead_color = (255, 255, 255)
        self.alive_color = (0, 0, 0)
        self.running = True
        self.paused = True
        self.speed = 8

        # Initialize game and button manager
        self.game = GameOfLife(grid_size)
        self.game.init_life()
        self.button_manager = ButtonManager(self.width, self.height - self.banner_height)


    def draw_grid(self):

        for y in range(self.grid_size[0]):
            for x in range(self.grid_size[1]):
                color = self.alive_color if self.game.generation[y, x] == 1 else self.dead_color
                pygame.draw.rect(
                    self.screen,
                    color,
                    (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                )


    def run(self):

        clock = pygame.time.Clock()

        while self.running:
            self.screen.fill(self.dead_color)
            self.draw_grid()
            self.button_manager.draw(self.screen)
            
            # Handle events and update game state
            self.handle_events()
            if not self.paused:
                self.game.next_generation()
                
            pygame.display.flip()
            clock.tick(int(self.speed))

        pygame.quit()


    def handle_events(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == MOUSEBUTTONDOWN:
                clicked_button = self.button_manager.get_clicked_button(event.pos)
                self.handle_button_click(clicked_button)


    def handle_button_click(self, button_name):

        if button_name == "play":
            self.paused = False
        elif button_name == "pause":
            self.paused = True
        elif button_name == "reset":
            self.game.init_life()
            self.speed = 8
        elif button_name == "speed_up":
            self.speed *= 1.1
            if self.speed > 20: self.speed = 20
        elif button_name == "slow_down":
            self.speed *= 0.9
            if self.speed < 1.0: self.speed = 1.0


if __name__ == "__main__":

    print('Hello, home!')
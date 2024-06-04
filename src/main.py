import pygame
from pygame import Surface
from pygame.time import Clock

from .settings import Settings


class Pygame:
    def __init__(self, settings: Settings) -> None:
        self.running: bool = True
        self.clock: Clock = pygame.time.Clock()
        self.fps: int = settings.fps
        self.window_width: int = settings.window_width
        self.window_height: int = settings.window_height
        self.window_title: str = settings.window_title

    @property
    def current_fps(self) -> float:
        return self.clock.get_fps()

    def update_window_title(self, title: str) -> None:
        pygame.display.set_caption(title=title)

    def update_window_size(self, width: int, height: int) -> None:
        self.window: Surface = pygame.display.set_mode((width, height))

    def display_fps(self) -> None:
        font = pygame.font.Font(None, size=36)
        fps_text: Surface = font.render(f'FPS {self.current_fps}', True, (0, 0, 0))
        self.window.blit(source=fps_text, dest=(10, 10))

    def run(self) -> None:
        pygame.init()
        self.update_window_size(width=self.window_width, height=self.window_height)
        self.update_window_title(title=self.window_title)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.window.fill(color='purple')
            self.display_fps()

            self.clock.tick(self.fps)
            pygame.display.flip()

        pygame.quit()

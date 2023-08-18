import sys
import pygame

from src.drive_c.api.Monitor import Monitor

from src.drive_c.api.Desktop import DesktopHandler
from src.drive_c.NitroOS.login_screen import LoginDesktop

class NitroOS:
    def __init__(self) -> None:
        self.output_res = (1600, 900)
        self.output_fps = 60

        self.monitor = Monitor(self.output_res, 60)
        self.clock = pygame.time.Clock()

        # Desktop
        self.desktop_handler = DesktopHandler()
        self.desktop_handler.add_desktop(LoginDesktop(0, self.output_res))

        self.running = True

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def update(self) -> None:
        pass

    def draw(self) -> None:
        self.desktop_handler.draw(self.monitor.output_surface)

        pygame.display.update()
        self.clock.tick(self.output_fps)

    def loop(self) -> None:
        while self.running:
            self.events()
            self.update()
            self.draw()

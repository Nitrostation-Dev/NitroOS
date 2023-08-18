import pygame

from src.drive_c.api.Desktop import Desktop

class LoginDesktop(Desktop):
    def __init__(self, id: int, size: (int, int)) -> None:
        super().__init__(id, size)

    def draw(self, output_surface: pygame.Surface) -> None:
        self.surface.fill((0, 255, 0))

        return super().draw(output_surface)
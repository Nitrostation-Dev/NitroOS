import pygame

from src.drive_c.api.Window import WindowNoDecorRounded


class LoginScreenDetails(WindowNoDecorRounded):
    def draw(self, output_surface: pygame.Surface) -> None:
        self.surface.fill((175, 175, 175))

        return super().draw(output_surface)

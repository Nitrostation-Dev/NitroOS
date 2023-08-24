import pygame

from src.drive_c.api.Desktop import Desktop
from src.drive_c.nitro_os.login_screen.windows import LoginScreenDetails
from src.drive_c.api.AssestManager import AssetManager


class LoginDesktop(Desktop):
    def __init__(
        self, id: int, size: (int, int), assets: AssetManager, desktop_handler
    ) -> None:
        super().__init__(id, size, assets)

        self.create_window(
            LoginScreenDetails, size=(500, 250), desktop_handler=desktop_handler
        )

    def draw(self, output_surface: pygame.Surface) -> None:
        self.surface.fill((0, 0, 0))

        return super().draw(output_surface)

import pygame

from src.drive_c.api.Desktop import Desktop
from src.drive_c.NitroOS.login_screen.windows import LoginScreenDetails
from src.drive_c.api.AssestManager import AssetManager

class LoginDesktop(Desktop):
    def __init__(self, id: int, size: (int, int), assets: AssetManager) -> None:
        super().__init__(id, size, assets)

        self.add_window(
            LoginScreenDetails(
                self.gen_id, title="Login Details", size=(300, 150), pos=(30, 30)
            )
        )

    def draw(self, output_surface: pygame.Surface) -> None:
        self.surface.fill((0, 255, 0))

        return super().draw(output_surface)

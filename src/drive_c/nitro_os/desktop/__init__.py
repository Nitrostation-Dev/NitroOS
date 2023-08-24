import pygame
from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.Desktop import Desktop


class NitroDesktop(Desktop):
    def __init__(self, id: int, size: (int, int), assets: AssetManager) -> None:
        super().__init__(id, size, assets)

        self.wallpaper = self.assets.get_asset("desktop_wallpaper")

    def draw(self, output_surface: pygame.Surface) -> None:
        self.surface.blit(self.wallpaper, (0, 0))

        return super().draw(output_surface)

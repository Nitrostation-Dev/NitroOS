import pygame
from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.Desktop import Desktop


class NitroDesktop(Desktop):
    def __init__(
        self, id: int, size: (int, int), assets: AssetManager, user_assets: AssetManager
    ) -> None:
        super().__init__(id, size, assets)

        self.user_assets = user_assets

        self.wallpaper = self.user_assets.get_asset("wallpaper")

    def draw(self, output_surface: pygame.Surface) -> None:
        self.surface.blit(self.wallpaper, (0, 0))

        return super().draw(output_surface)

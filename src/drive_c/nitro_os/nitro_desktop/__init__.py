import pygame
from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.Desktop import Desktop

from src.drive_c.nitro_os.nitro_desktop.gui import Taskbar


class NitroDesktop(Desktop):
    def __init__(
        self, id: int, size: (int, int), assets: AssetManager, user_assets: AssetManager
    ) -> None:
        super().__init__(id, size, assets)

        self.user_assets = user_assets

        self.wallpaper = self.user_assets.get_asset("wallpaper")
        self.taskbar = Taskbar(0, self.assets)

    def events(self, event) -> None:
        self.taskbar.events(event)

        return super().events(event)
    
    def update(self) -> None:
        self.taskbar.update()

        return super().update()

    def draw(self, output_surface: pygame.Surface) -> None:
        self.surface.blit(self.wallpaper, (0, 0))

        self.taskbar.draw(self.surface)

        return super().draw(output_surface)

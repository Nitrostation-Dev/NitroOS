import pygame
from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.Desktop import Desktop

from src.drive_c.nitro_os.desktops.nitro_desktop.gui import Taskbar


class NitroDesktop(Desktop):
    def __init__(
        self, id: int, size: (int, int), assets: AssetManager
    ) -> None:
        super().__init__(id, size, assets)

        self.wallpaper = self.assets.get_asset("wallpaper")
        self.taskbar = Taskbar(0, self.assets)

    def events(self, event) -> None:
        self.taskbar.events(event)

        return super().events(event)
    
    def update(self, delta: float) -> None:
        self.taskbar.update(delta)

        return super().update(delta)

    def draw(self, output_surface: pygame.Surface) -> None:
        self.surface.blit(self.wallpaper, (0, 0))

        self.taskbar.draw(self.surface)

        return super().draw(output_surface)

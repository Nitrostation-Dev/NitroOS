import pygame

from src.drive_c.api.AssestManager import AssetManager


class GuiElement:
    def __init__(
        self, name: str, pos: (int, int), asset_manager: AssetManager, **kargs
    ) -> None:
        self.name = name
        self.pos = pos
        self.assest_manager = asset_manager

        self.__dict__.update(kargs)

    def events(self, event) -> None:
        pass

    def update(self) -> None:
        pass

    def draw(self, output_surface: pygame.Surface) -> None:
        pass

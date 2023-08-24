from enum import Enum
import pygame

from src.drive_c.api.AssestManager import AssetManager

class FontStyle(Enum):
    REGULAR = 1
    ITALIC = 2
    BOLD = 3

class PostitionType(Enum):
    TOPLEFT = 1
    MIDLEFT = 2
    CENTER = 3


class GuiElement:
    def __init__(
        self, name: str, pos: (int, int), asset_manager: AssetManager, **kargs
    ) -> None:
        self.name = name
        self.pos = pos
        self.pos_type = PostitionType.TOPLEFT
        self.asset_manager = asset_manager

        self.__dict__.update(kargs)

    def events(self, event) -> None:
        pass

    def update(self) -> None:
        pass

    def draw(self, output_surface: pygame.Surface) -> None:
        pass

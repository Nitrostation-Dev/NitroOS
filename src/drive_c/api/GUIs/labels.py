import pygame

from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.GUIs import GuiElement


class GuiElementLabel(GuiElement):
    def __init__(
        self, name: str, pos: (int, int), asset_manager: AssetManager, **kargs
    ) -> None:
        self.font_family = self.assest_manager.get_asset("interface_font_family")
        self.font_size = self.assest_manager.get_asset("interface_font_size")

        super().__init__(name, pos, asset_manager, **kargs)

    def draw(self, output_surface: pygame.Surface) -> None:
        pass

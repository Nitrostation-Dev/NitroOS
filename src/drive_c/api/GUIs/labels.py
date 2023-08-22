import pygame

from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.GUIs import GuiElement, FontStyle


class GuiElementLabel(GuiElement):
    def __init__(
        self,
        name: str,
        pos: (int, int),
        asset_manager: AssetManager,
        message: str,
        **kargs
    ) -> None:
        self.asset_manager = asset_manager
        self.font_style = FontStyle.REGULAR
        self.message = message

        super().__init__(name, pos, asset_manager, **kargs)

        if self.font_style == FontStyle.REGULAR:
            self.font_family = self.asset_manager.get_asset(
                "interface_font_family_regular"
            )

        elif self.font_style == FontStyle.ITALIC:
            self.font_family = self.asset_manager.get_asset(
                "interface_font_family_italic"
            )

        elif self.font_style == FontStyle.BOLD:
            self.font_family = self.asset_manager.get_asset(
                "interface_font_family_bold"
            )

        self.fg_color = self.asset_manager.get_asset("interface_text_fg_color")

        self.surface = self.font_family.render(message, True, self.fg_color)
        self.rect = self.surface.get_rect(topleft=pos)

    def update_message(self, message: str) -> None:
        self.message = message
        self.surface = self.font_family.render(message, True, self.fg_color)

    def draw(self, output_surface: pygame.Surface) -> None:
        output_surface.blit(self.surface, self.rect)

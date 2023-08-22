import pygame

from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.GUIs import FontStyle
from src.drive_c.api.Window import WindowNoDecorRounded
from src.drive_c.api.GUIs.labels import GuiElementLabel


class LoginScreenDetails(WindowNoDecorRounded):
    def __init__(self, id: int, assets: AssetManager, **kargs) -> None:
        super().__init__(id, assets, **kargs)

        self.title_label = GuiElementLabel(
            "title_label",
            (10, 10),
            self.assets,
            "Enter Login Details",
            font_style=FontStyle.BOLD,
        )

        self.username_label = GuiElementLabel(
            "username_label",
            (10, 50),
            self.assets,
            "Username: "
        )

        self.password_label = GuiElementLabel(
            "password_label",
            (10, 80),
            self.assets,
            "Password: "
        )

    def draw(self, output_surface: pygame.Surface) -> None:
        self.surface.fill((220, 220, 220))

        self.title_label.draw(self.surface)
        self.username_label.draw(self.surface)
        self.password_label.draw(self.surface)

        return super().draw(output_surface)

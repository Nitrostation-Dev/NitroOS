import pygame

from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.GUIs import FontStyle, PostitionType
from src.drive_c.api.Window import WindowNoDecorRounded

from src.drive_c.api.GUIs.labels import GuiElementLabel
from src.drive_c.api.GUIs.input_field import GuiElementInputField


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
            (10, 70),
            self.assets,
            "Username: ",
            pos_type=PostitionType.MIDLEFT

        )

        self.password_label = GuiElementLabel(
            "password_label",
            (10, 110),
            self.assets,
            "Password: ",
            pos_type=PostitionType.MIDLEFT
        )

        self.username_field = GuiElementInputField(
            "username_field",
            (150, 70),
            self.assets,
            "username",
            pos_type=PostitionType.MIDLEFT
        )
        self.password_field = GuiElementInputField(
            "password_field",
            (150, 110),
            self.assets,
            "password",
            pos_type=PostitionType.MIDLEFT,
            is_pass=True
        )

    def events(self, event) -> None:
        self.username_field.events(event)
        self.password_field.events(event)

    def update(self) -> None:
        self.username_field.update()
        self.password_field.update()

    def draw(self, output_surface: pygame.Surface) -> None:
        self.surface.fill((220, 220, 220))

        self.title_label.draw(self.surface)
        self.username_label.draw(self.surface)
        self.password_label.draw(self.surface)
        
        self.username_field.draw(self.surface)
        self.password_field.draw(self.surface)

        return super().draw(output_surface)

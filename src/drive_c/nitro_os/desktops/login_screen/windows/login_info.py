import pygame

from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.GUIs import FontStyle, PositionType
from src.drive_c.api.GUIs.buttons import GuiElementButton
from src.drive_c.api.Window import WindowNoDecorRounded

from src.drive_c.api.GUIs.labels import GuiElementLabel
from src.drive_c.api.GUIs.input_field import GuiElementInputField

from src.drive_c.nitro_os.encryption import decrypt_str


class LoginScreenDetails(WindowNoDecorRounded):
    def __init__(
        self,
        id: int,
        assets: AssetManager,
        change_user_func=None,
        **kargs,
    ) -> None:
        super().__init__(id, assets, size=(480, 200))

        self.change_user_func = change_user_func

        self.__dict__.update(kargs)

        # Labels
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
            pos_type=PositionType.MIDLEFT,
        )
        self.password_label = GuiElementLabel(
            "password_label",
            (10, 110),
            self.assets,
            "Password: ",
            pos_type=PositionType.MIDLEFT,
        )

        # Input Fields
        self.username_field = GuiElementInputField(
            "username_field",
            (150, 70),
            self.assets,
            "username",
            input_text="default" ,
            pos_type=PositionType.MIDLEFT,
        )
        self.password_field = GuiElementInputField(
            "password_field",
            (150, 110),
            self.assets,
            "password",
            is_active=True,
            pos_type=PositionType.MIDLEFT,
            is_pass=True,
        )

        # Buttons
        self.login_button = GuiElementButton(
            "login_button",
            (self.rect.width / 2, 165),
            self.assets,
            "Login",
            self.login,
            pos_type=PositionType.CENTER,
        )

        # Wallpaper
        self.wallpaper = self.assets.get_asset("login_wallpaper")

    def login(self):
        login_details = self.assets.get_asset("login_details")
        input_username = self.username_field.input_text
        input_password = self.password_field.input_text

        for login_detail in login_details:
            if login_detail["username"] != input_username:
                continue

            if decrypt_str(login_detail["key"], login_detail["pass"]) != input_password:
                pass  # TODO: Implement Small message that says login failed

            else:
                self.change_user_func(input_username)

    def events(self, event) -> None:
        self.username_field.events(event)
        self.password_field.events(event)

        self.login_button.events(event)

    def draw(self, output_surface: pygame.Surface) -> None:
        self.surface.fill((250, 250, 250))

        output_surface.blit(self.wallpaper, (0, 0))

        self.title_label.draw(self.surface)
        self.username_label.draw(self.surface)
        self.password_label.draw(self.surface)

        self.username_field.draw(self.surface)
        self.password_field.draw(self.surface)

        self.login_button.draw(self.surface)

        return super().draw(output_surface)

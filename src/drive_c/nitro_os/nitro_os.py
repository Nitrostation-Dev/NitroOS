from json import JSONDecodeError
import sys
import os
import time
import pygame

from src.drive_c.api.Monitor import Monitor
from src.drive_c.api.Desktop import DesktopHandler
from src.drive_c.api.AssestManager import AssetManager

from src.drive_c.nitro_os.read_json import get_json_data
from src.drive_c.nitro_os.desktops import LoginDesktop, NitroDesktop
from src.drive_c.nitro_os.applications import appsData


class NitroOS:
    def __init__(self) -> None:
        self.running = True

        # Monitor
        self.output_res = (1600, 900)
        self.output_fps = 60
        self.monitor = Monitor(self.output_res)
        self.clock = pygame.time.Clock()

        # Get All User Logins Data
        login_details = []

        user_folders = os.listdir("src/drive_c/users/")
        for folder in user_folders:
            try:
                user_data = get_json_data(
                    "src/drive_c/users/" + folder + "/data/login_details.json"
                )
            except JSONDecodeError:
                self.running = False
                print(
                    'Error reading "{0}"'.format(
                        "src/drive_c/users/" + folder + "/data/login_details.jsonc"
                    )
                )

            login_details.append(user_data)

        # Applications
        # System-Wide Applications
        self.system_apps_data = appsData

        # Icon Themes
        self.icons = {
            "applications": {},
        }
        app_icons = os.listdir(
            "src/drive_c/assets/icons/default_icon_pack/applications"
        )
        for icon in app_icons:
            self.icons["applications"][icon.split(".")[0]] = pygame.image.load(
                "src/drive_c/assets/icons/default_icon_pack/applications/" + icon
            ).convert_alpha()

        # Assets
        self.assets = AssetManager()
        self.user_assets = AssetManager()

        interface_font_size = 20
        desktop_wallpaper = pygame.Surface(self.output_res)
        desktop_wallpaper.fill((100, 100, 100))
        self.assets.update_assets(
            {
                # Monitor
                "monitor_size": self.output_res,
                "fps": self.output_fps,
                # Ui
                "interface_font_size": 20,
                "interface_font_family_regular": pygame.font.Font(
                    "src/drive_c/assets/fonts/Ubuntu-Regular.ttf", interface_font_size
                ),
                "interface_font_family_italic": pygame.font.Font(
                    "src/drive_c/assets/fonts/Ubuntu-Italic.ttf", interface_font_size
                ),
                "interface_font_family_bold": pygame.font.Font(
                    "src/drive_c/assets/fonts/Ubuntu-Bold.ttf", interface_font_size
                ),
                "interface_text_fg_color": (0, 0, 0),
                # Login
                "login_details": login_details,
                # Wallpapers
                "login_wallpaper": pygame.transform.scale(
                    pygame.image.load(
                        "src/drive_c/assets/wallpapers/unsplash-login.jpg"
                    ),
                    self.output_res,
                ),
                "desktop_wallpaper": desktop_wallpaper,
                # Taskbar
                "taskbar_height": 40,
                "taskbar_border_radius": 8,
                "taskbar_margin": (2, 2),
                "taskbar_bg_color": (180, 180, 235),
                "taskbar_transparency": 225,
                # Handle Installed Apps
                "apps": self.system_apps_data,
                "launch_app": self.launch_app,
                # Icons
                "icons": self.icons,
                "get_icon": self.get_icon_for_app,
                # Windows
                "window_opening_initial_velocity": 7500,
            }
        )
        self.user_assets.update_assets(self.assets.get_assets())

        # Desktops
        self.desktop_handler = DesktopHandler()
        self.desktop_handler.add_desktop(
            LoginDesktop(
                0,
                self.output_res,
                self.assets,
                self.update_current_user,
            )
        )

        # System Resources
        self.prev_time = time.time()

    def get_icon_for_app(self, name: str) -> pygame.Surface:
        for icon in self.icons["applications"]:
            if icon != name:
                continue

            return self.icons["applications"][icon]

    def launch_app(self, app_class) -> None:
        self.desktop_handler.desktops[1].create_window(
            app_class
        )  # TODO: Implement Better App Launch System

    def final_init(self) -> None:
        self.desktop_handler.final_init()

    def update_current_user(self, username: str) -> None:
        for login_data in self.assets.get_asset("login_details"):
            if login_data["username"] != username:
                continue

            # UserAssets
            self.user_assets.update_assets(self.assets.get_assets())

            self.user_assets.update_assets(
                get_json_data(
                    "src/drive_c/users/"
                    + login_data["username"]
                    + "/data/os_settings.json"
                )
            )
            self.user_assets.update_assets({"login_data": login_data})
            self.user_assets.update_assets(
                {
                    "wallpaper": pygame.transform.scale(
                        pygame.image.load(self.user_assets.get_asset("wallpaper")),
                        self.output_res,
                    )
                }
            )

            self.desktop_handler.add_desktop(
                NitroDesktop(1, self.output_res, self.user_assets)
            )
            self.desktop_handler.change_to_desktop(1)

            return

        raise ValueError("NO USER!")

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            self.desktop_handler.events(event)

    def update(self) -> None:
        current_time = time.time()
        delta = current_time - self.prev_time
        self.prev_time = time.time()

        self.desktop_handler.update(delta)

    def draw(self) -> None:
        self.desktop_handler.draw(self.monitor.output_surface)

        pygame.display.update()
        self.clock.tick(self.output_fps)

    def loop(self) -> None:
        self.final_init()

        while self.running:
            self.events()
            self.update()
            self.draw()

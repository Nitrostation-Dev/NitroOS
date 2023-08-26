from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.Window import WindowNoDecorRounded


class Taskbar(WindowNoDecorRounded):
    def __init__(self, id: int, assets: AssetManager, **kargs) -> None:
        super().__init__(id, assets, **kargs)

        self.border_radius = 24

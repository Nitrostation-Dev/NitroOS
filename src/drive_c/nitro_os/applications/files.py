from src.drive_c.api.AssestManager import AssetManager
from src.drive_c.api.Window import Window


class FilesApp(Window):
    def __init__(self, id: int, assets: AssetManager, **kargs) -> None:
        super().__init__(id, assets, size=(1000, 800), **kargs)

    def events(self, event) -> None:
        pass

appPackage = {"name": "Files", "icon_name": "files", "class": FilesApp}

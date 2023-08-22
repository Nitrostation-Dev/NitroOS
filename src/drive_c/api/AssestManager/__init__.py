class AssetManager:
    def __init__(self, **kargs) -> None:
        self.assets = {}

        self.assets.update(kargs)

    def add_asset(self, name: str, value: any) -> None:
        self.assets.update({name: value})

    def update_asset(self, dict) -> None:
        self.assets.update(dict)

    def get_assets(self) -> any:
        return self.assets

    def get_asset(self, name: str):
        return self.assets.get(name)

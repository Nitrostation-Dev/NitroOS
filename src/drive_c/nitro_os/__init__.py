from src.drive_c.nitro_os.nitro_os import NitroOS

def start_os() -> None:
    nitro_os = NitroOS()

    nitro_os.loop()

import sys


class WrongOsError(Exception):
    pass

def encoding_error():
    mssg=f"EXCEPTION: There is a problem with the reading of the file. It can be the encoding"
    print(mssg)

def windows_interaction():
    if not sys.platform.startswith("win"):
        raise WrongOsError(f"⛔️ Windows only. Your system: '{sys.platform}'.")
    print("🪟 Doing important Windows work.")


def macos_interaction():
    if not sys.platform.startswith("darwin"):
        raise WrongOsError(f"⛔️ macOS only. Your system: '{sys.platform}'.")
    print("🍏 Doing important macOS work.")


def linux_interaction():
    if not sys.platform.startswith("linux"):
        raise WrongOsError(f"⛔️ Linux only. Your system: '{sys.platform}'.")
    print("🐧 Doing important Linux work.")

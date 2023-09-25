import sys


class WrongOsError(Exception):
    pass


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

from sys import platform

def system_check():
    if platform == "linux":
        return "linux"
    if platform == "win32":
        return "windows"
    if platform == "darwin":
        return "mac"


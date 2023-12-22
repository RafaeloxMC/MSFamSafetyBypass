import sys
from cx_Freeze import setup, Executable

setup(
    name = "MS FamSafety Bypass",
    version = "1.0",
    description = "MS FamSafety Bypass",
    executables = [Executable("bypass.py", base = "Console")])
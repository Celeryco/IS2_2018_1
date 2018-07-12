import sys
import os
from data import tools
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
pic_list = tools.get_pics(os.path.join("resources", "graphics"))
build_exe_options = {"packages": ["os", "pygame", "pytmx"], "include_files": ['data/', 'resources/', 'maps/']}
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None;
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Peruvian Heart DE",
        version = "0.1",
        description = "Peruvian Heart DE!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("peruvian_heart.py", base=base)])

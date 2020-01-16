## TODO: EFFICIENCY: Make a more detailed installer to only include modules needed from each package.

#run 'python setup.py bdist_msi' to create a windows installer

import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['stringdist', 'pytesseract', 'os', 'cv2', 'numpy', 'sys', 'networkx', 'PIL', 'matplotlib', 'pickle'], 'include_files': ['code/utils.py', 'code/profile.py', 'code/maps.py'], "include_msvcr": True}

#Set base to console
base = None

setup(
    name = 'R6LocationTracker',
    version = '0.0',
    description = '',
    options = {'build_exe': build_exe_options},
    executables = [Executable('code/dev.py', base=base)]
)

import shutil
import os

def configure_dedupe():
    path = os.getcwd() + '\\lib_dedupe\\convenience.py'
    dest = os.getenv("LIB_PYTHON")+"\\dedupe\\convenience.py"
    shutil.copy(str(path), str(dest)) 

configure_dedupe()
import sys
import os
from NewsProject.wsgi import application

INTERP = os.path.expanduser("~/venv/Scripts")

if sys.executable != INTERP: 
    os.execl(INTERP, INTERP, *sys.argv)


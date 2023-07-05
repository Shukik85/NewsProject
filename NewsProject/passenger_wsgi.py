import sys, os
INTERP = os.path.expanduser("~/venv311/bin/python3")

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from NewsProject.wsgi import application

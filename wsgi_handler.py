import os, sys

os.chdir(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__))

import app

application = app.default_app()

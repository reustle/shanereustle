from bottle import debug, route, static_file, run, error, default_app
import settings
from views.about import *
from views.projects import *
from views.clients import *
from views.contact import *
from views.blog import *

debug(settings.DEBUG)

@route("/static/:filename#.*#")
def static(filename):
	return static_file(filename, root=settings.PROJECT_PATH+"/static")

if __name__ == "__main__":
	run( reloader=settings.AUTO_RELOAD )
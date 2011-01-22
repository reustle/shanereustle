from bottle import debug, route, static_file, run, default_app
import settings
from controllers.index import *
from controllers.email import *

debug(settings.DEBUG)

@route("/static/:filename#.*#")
def static(filename):
	return static_file(filename, root=settings.PROJECT_PATH+"/static")

if __name__ == "__main__":
	run( reloader=settings.AUTO_RELOAD )


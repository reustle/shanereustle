from bottle import view, route

@route("/")
@view("templates/about")
def view_about():
	return {"meta_title":"Professional Geek"}

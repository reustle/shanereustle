from bottle import view, route, redirect

@route("/projects/")
@view("templates/projects")
def view_projects():
	return {"meta_title":"Projects"}

@route("/projects")
def redirect_projects():
	redirect("/projects/")
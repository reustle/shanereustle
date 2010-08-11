from bottle import view, route, redirect

@route("/contact/")
@view("templates/contact")
def view_contact():
	return {"meta_title":"Contact Information"}

@route("/contact")
def redirect_contact():
	redirect("/contact/")
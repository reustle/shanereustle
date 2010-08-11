from bottle import view, route, request, response, redirect
from models import AccountsClass

accounts = AccountsClass()

@route("/clients/")
@route("/clients/", method="POST")
@view("templates/clients")
def view_clients():
	output = {"meta_title":"Clients","section":"login_page"}
	
	logged_in = False
	
	if request.forms.get("login_email"):
		# They are trying to log in
		
		login_email = request.forms.get("login_email")
		login_password = request.forms.get("login_password")
	
		if len(login_email) > 4 and len(login_password) > 4:
			if accounts.try_login( login_email , login_password ):
				response.set_cookie( "reustle_hash" , login_email )
				logged_in = True
	
	if request.COOKIES.get("reustle_hash") or logged_in:
		if request.COOKIES.get("reustle_hash") != "":
			output.update({"section":"dashboard"})
	
	return output

@route("/clients/logout")
def view_clients_logout():
	response.set_cookie( "reustle_hash" , "" )
	redirect("/clients/")
	
@route("/clients")
def redirect_clients():
	redirect("/clients/")
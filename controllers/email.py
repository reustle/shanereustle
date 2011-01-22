from bottle import view, route, request

@route("/email/", method="POST")
def send_mail():
	# In progress
	return "Hello " + request.GET["name"]

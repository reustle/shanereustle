from bottle import view, route, request
import smtplib

@route("/email/", method="POST")
def send_mail():
	post_name = request.POST.get("name")
	post_email = request.POST.get("email")
	post_phone = request.POST.get("phone")
	post_message = request.POST.get("message")
	
	smtp = smtplib.SMTP("localhost")
	message = "Name: " + post_name + "\n"
	message += "Email: " + post_email + "\n"
	message += "Phone: " + post_phone + "\n"
	message += "Message: " + post_message + "\n"
	
	smtp.sendmail("ShaneReustle.com Contact Form <noreply@shanereustle.com>", "sreustle@gmail.com", "message")
	
	smtp.quit()
	
	return "Hello " + request.GET["name"]


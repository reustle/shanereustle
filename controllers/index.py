from bottle import view, route

@route('/')
@view('templates/index')
def view_index():
	return {}


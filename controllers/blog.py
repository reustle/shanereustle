from bottle import view, route, template
import settings

@route('/blog/:entry/')
def view_blog(entry=None):
	if entry:
		handle = open( settings.PROJECT_PATH  + '/templates/blog/' + entry + '.html')
		contents = handle.readlines()
		handle.close()
		title = contents[1].replace('<h1>', '').replace('</h1>', '')
		
		return template('templates/blog/' + entry, title=title)
	

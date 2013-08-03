import pystache
import json
from flask import Flask, redirect
import settings as SETTINGS
app = Flask(__name__)

# Routing & Controllers
@app.route('/')
def blog_index(blog_page=1):
	""" The list of blog entries """
	
	return redirect('http://reustle.io', 301)
	
@app.route('/blog/<slug>.html')
def blog_entry(slug):
	""" Redirect Blog Entries """
	
	if slug == 'freelance-software-engineer':
		slug = 'freelance-software-developer'
	
	return redirect('http://reustle.io/blog/' + slug, 301)

if __name__ == '__main__':
	app.run(port=SETTINGS.port, debug=True)


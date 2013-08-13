import pystache
import json
from flask import Flask, abort
import settings as SETTINGS
app = Flask(__name__)

# General Functions
def read_file(filename):
	""" Simply read a file """
	
	project_path = SETTINGS.project_path
	
	file_handle = open(project_path + filename)
	file_contents = file_handle.read()
	file_handle.close()
	
	return file_contents.encode('utf-8')
	
def load_template(template_params):
	""" Load the template and apply the given parameters """
	
	template_html = read_file('template.html')

	return pystache.render(template_html, template_params)

def load_blog_index():
	""" Load an article """
	
	raw_json = read_file('articles/index.json')
	blog_index_json = json.loads(raw_json)
	
	# Load the content of each article
	for article in blog_index_json:
		article['content'] = read_file('articles/' + article['slug'] + '.html')
	
	return blog_index_json


# Routing & Controllers
@app.route('/')
def blog_index(blog_page=1):
	""" The list of blog articles and their content """
	
	articles_per_page = 4
	articles = load_blog_index()
	
	offset = blog_page - 1
	
	start = offset * articles_per_page
	end = start + articles_per_page
	
	last_page = False
	if end >= len(articles):
		last_page = True
	
	articles = articles[start:end]
	
	next_page = False
	if blog_page > 1:
		next_page = blog_page - 1
	
	prev_page = False
	if not last_page:
		prev_page = blog_page + 1
	
	return load_template({
		'index_page' : True,
		'prev_page' : prev_page,
		'next_page' : next_page,
		'articles' : articles
	})

@app.route('/blog/')
def blog_list():
	""" Display a list of all articles """
	
	articles = load_blog_index()
	
	return load_template({
		'list_page' : True,
		'articles_list' : articles
	})

@app.route('/blog/page<int:blog_page>/')
def blog_index_older(blog_page):
	""" Show an older blog index page """
	
	return blog_index(blog_page)

@app.route('/blog/<slug>')
def blog_article(slug):
	""" An individual blog article """
	
	# TODO articles index file? something?
	
	blog_index = load_blog_index()
	
	article_data = False
	for article in blog_index:
		if article['slug'].lower() == slug.lower():
			article_data = article
	
	if not article_data:
		
		return abort(404)
	
	return load_template({
		'articles' : [article_data]
	})

if __name__ == '__main__':
	app.run(port=SETTINGS.port, debug=True)


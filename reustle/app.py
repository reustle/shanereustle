import pystache
import json
from flask import Flask, abort, redirect
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
	
def load_template(template_params, filename='template'):
	""" Load the template and apply the given parameters """
	
	template_html = read_file('templates/' + filename + '.html')

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
	
	return load_template({}, filename='splash')

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

@app.route('/blog/<slug>.html')
def blog_article_legacy(slug):
	"""
		ShaneReustle.com/blog/article-name.html redirects
		to Reustle.io/blog/article-name.html, remove the
		.html with a 301 redirect
	"""
	
	# Handle freelance blog post name change
	if slug == 'freelance-software-engineer':
		slug = 'freelance-software-developer'
	
	article_url = '/blog/' + slug
	
	return redirect(article_url, 301)

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


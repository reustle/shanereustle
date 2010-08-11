from bottle import view, route, redirect
from models import BlogClass

blog = BlogClass()

# Blog Index (To Add: Pagination)
@route("/blog/")
@route("/blog")
@view("templates/blog")
def view_blog():
	output = {
		"meta_title":"Blog",
		"entries": blog.get_entries()
	}
	
	return output

# Individual Entry (To Add: Meta Keywords)
@route("/blog/:entry_query/")
@route("/blog/:entry_query")
@view("templates/blog_entry")
def view_blog_entry(entry_query):
	output = {
		"meta_title":"Blog",
		"entry": blog.get_entry(entry_query)
	}
	output["meta_title"] = output["entry"]["title"]
	
	output["entry"]["timestamp"] = output["entry"]["timestamp"].strftime("%B %e %Y")
	
	return output

# Search Index (To Add: Search Box, Smarter Search)
@route("/blog/search/")
@route("/blog/search")
@view("templates/blog_search")
def view_blog_search():
	output = {
		"meta_title":"Blog Search",
		"search_query":"",
		"keywords":blog.list_keywords()
	}

	return output

# Search Results
@route("/blog/search/:search_query")
@route("/blog/search/:search_query/")
@view("templates/blog_search")
def view_blog_search_results(search_query="none"):
	output = {
		"meta_title":"Blog Search Results: "+search_query,
		"search_query": search_query,
		"entries": blog.search_entries(search_query)
	}
	for entry in output["entries"]:
		entry["timestamp"] = entry["timestamp"].strftime("%b %e %Y")
	
	return output

# Archive Page
@route("/blog/archive/")
@route("/blog/archive")
@view("templates/blog_archive")
def view_blog_archive():
	output = {
		"meta_title":"Blog Archive",
		"entries":blog.get_entries()
	}
	for entry in output["entries"]:
		entry["timestamp"] = entry["timestamp"].strftime("%b %e %Y")
	
	return output

"""
<p>I have been working with Django for the past few months, and it is a great project with a great community, but I'm starting to think it isn't the right tool for every project. I have always been a minimalist, and that is reflected in my code. One of my active projects is running on Django and I'm glad I used it, but most of my projects aren't that large. This is where I started to think about using smaller frameworks for my smaller projects, which lead me to the world of micro frameworks.</p>
<p>I did some research on popular Python micro web frameworks over the past few days, and after digging into a few of the projects, <a href=\"http://bottle.paws.de/\">Bottle.py</a> caught my eye. Bottle aims to be a fast, simple and lightweight framework, and it does just that. The entire framework is contained in a single file, and only include the basic functionality need to get a site up and running. This was a perfect fit for me since I was wasn't using any Django specific functionality anyway. Its URL routing is dead simple, as well as its <a href=\"http://bottle.paws.de/docs/dev/stpl.html\">SimpleTemplate engine</a>. Here is an example of an app that returns Hello World.</p>
<pre><code class=\"python\"><span class=\"keyword\">from</span> bottle <span class=\"keyword\">import</span> route, run

<span class=\"decorator\">@route(\"/\")</span>
<span class=\"function\"><span class=\"keyword\">def</span> <span class=\"title\">index</span><span class=\"params\">()</span>:</span>
    <span class=\"keyword\">return</span> <span class=\"string\">\"Hello World!\"</span>

run()</code></pre>
<p>I love the use of decorators for URL routing, and it makes easy to take URL arguments too. Anyway, I liked Bottle.py so much, I decided to use it to write the blog you are currently on. It took me one evening to finish, and I am more than happy with how it turned out. Another exciting thing about the blog is that it is my first site in production using <a href=\"http://mongodb.org\">MongoDB</a>. I will go into more detail about my experience sofar with MongoDB in a later blog post.</p>
<p>If you didn't know, the source of the site is <a href=\"http://bitbucket.org/crath/shanereustle.com/\">available here</a>.</p>
"""

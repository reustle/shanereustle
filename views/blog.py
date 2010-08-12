from bottle import view, route, redirect, abort
from models import BlogClass
import settings

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
	if output["entry"] == None:
		abort(404, "Blog entry not found.")
	
	output["meta_title"] = output["entry"]["title"]
	
	output["entry"]["timestamp"] = output["entry"]["timestamp"].strftime( settings.DATE_FORMAT )
	
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
def view_blog_search_results(search_query):
	output = {
		"meta_title":"Blog Search Results: "+search_query,
		"search_query": search_query,
		"entries": blog.search_entries(search_query)
	}
	for entry in output["entries"]:
		entry["timestamp"] = entry["timestamp"].strftime( settings.DATE_FORMAT )
	
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
		entry["timestamp"] = entry["timestamp"].strftime( settings.DATE_FORMAT )
	
	return output
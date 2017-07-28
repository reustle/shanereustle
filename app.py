from flask import Flask, redirect
app = Flask(__name__)


@app.route('/')
def home_redirect():
    return redirect('http://reustle.org/', code=301)

@app.route('/blog/')
def blog_redirect():
    return redirect('http://reustle.org/articles', code=301)

@app.route('/blog/<article>')
def blog_redirect(article):
    return redirect('http://reustle.org/'+article, code=301)


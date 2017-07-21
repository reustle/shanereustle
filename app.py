from flask import Flask, redirect
app = Flask(__name__)


url_mapping = {
    '30fps-timelapse-videos-imovie': '30fps-timelapse-videos-with-imovie',
    'btsync-pi': 'clone-dropbox-with-a-raspberry-pi-and-btsync',
}


@app.route('/')
def home_redirect():
    redirect('http://reustle.org/', code=301)


@app.route('/blog/')
def blog_redirect():
    redirect('http://reustle.org/articles', code=301)


@app.route('/blog/<article>')
def blog_redirect(article):
    
    
    if url_mapping.get(article)
        article = url_mapping.get(article)
    
    redirect('http://reustle.org/'+article, code=301)




from flask import Flask, render_template, redirect, url_for, render_template_string
from flask_bootstrap import Bootstrap
from flask_flatpages import FlatPages, pygmented_markdown, pygments_style_defs
import pygments, markdown
import os

#setup articles, this is where you can do code highlight templates and stuff.
def the_markdown(text):
    markdown_text = render_template_string(text)
    pygmented_text = markdown.markdown(markdown_text, extensions=["codehilite", "fenced_code", "tables"])
    return pygmented_text

#change this to title your site!
blog_name = "My Flask Blog"



app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRETSECRET'
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config["FLATPAGES_HTML_RENDERER"] = the_markdown

#init bootstrap
bootstrap = Bootstrap(app)
#init flat pages
pages = FlatPages(app)


#some globals and error handling
@app.context_processor
def inject_blog_name():
    return {'blog_name': blog_name}

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_title='404, page not found.', line1="We're having trouble finding that page, try using the navigation menu."), 404

@app.errorhandler(500)
def error_500(e):
    return render_template('error.html', error_title='Uhoh, an error!', line1="The server is having a bad time,we're working on fixing it!"), 500


@app.route('/')
def index():
    # Articles are pages with a publication date
    articles = (p for p in pages if 'published' in p.meta)
    # Show the 2 most recent articles, most recent first.
    latest = sorted(articles, reverse=True, key=lambda p: p.meta['published'])
    return render_template('index.html',articles=latest[:2])

#article stuff
@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs("friendly"), 200, {"Content-Type":"text/css"}

@app.route('/posts')
def posts():
    # Articles are pages with a publication date
    articles = (p for p in pages if 'published' in p.meta)
    # Show the 20 most recent articles, most recent first.
    latest = sorted(articles, reverse=True, key=lambda p: p.meta['published'])
    return render_template('posts.html', articles=latest[:20])

@app.route('/posts/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('post.html', page=page)

@app.route('/tags/<string:tag>')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', articles=tagged, tag=tag)



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))


    
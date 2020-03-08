# simple-flask-blog
A minimal markdown file based blog, written in flask.

Uses bootstrap-flask, so it's bootstrap4 not 3. and Flask-Flatpages, for the actual content parts.

I am reasonably sure this would work for github pages.

## to use
* clone this repo
* setup a python venv, using python -m venv env
    * active your env by typing `source env/bin/activate`
* run using python app.py

## customize me!
* this was setup using bootstrap-flask, so anything bootstrap can do [getboostrap.com], this blog can do.
* you'll find layout.html in the templates directory, thats where you should adjust most of your markup.

## write posts!
* posts are just markdown files, in the pages directory, it supports code highlighting and lots of other features you'd expect. 
* you can find an example blank one in the static directory.
* posts will auto sort by the published date in the .md file. the latest 2 appearing on the home page, and the latest 20 appearing on the posts page.



### todo
* pagination, but I'm not totally sure thats within the scope of this project.
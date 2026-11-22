from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/foobar')
def foobar():
    return "<span style='color:blue'>Hello again!</span>"

@app.route('/contact')
def contact():
    return render_template("contact.html")


# Drawings
@app.route('/drawings')
def drawings():
    return render_template("/drawings/drawings.html")

@app.route('/drawings/digital')
def digital():
    return render_template("/drawings/digital.html")

@app.route('/drawings/traditional')
def traditional():
    return render_template("/drawings/traditional.html")

# Photos

@app.route('/photos')
def photos():
    return render_template("/photos/photos.html")

@app.route('/photos/milo')
def milo():
    return render_template("/photos/milo.html")

@app.route('/photos/lay')
def lay():
    return render_template("/photos/lay.html")

    
@app.route('/projects')
def blog():
    return render_template("projects.html")

@app.route('/words')
def words():
    return render_template("words.html")

@app.route('/login')
def login():
    if not 'x-kvd-payload' in request.headers:
        url = 'https://api.uqcloud.net/login/https://' + request.headers['host'] + '/login'
        return redirect(url)
    userjson = request.headers['x-kvd-payload']
    user = json.loads(userjson)
    return redirect('https://zhubat.uqcloud.net')

 
if __name__ == '__main__':
    app.run()

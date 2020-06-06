from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "Home"


@app.route("/about")
def about():
    return "About page"


@app.route("/containers/")
def posts():
    return "List of all containers"


@app.route("/container/<int:container_id>")
def post_details(container_id):
    return "Container stats: %s" % container_id

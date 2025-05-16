from agent import stream_graph_updates
from options import init_options
from flask import Flask

options = init_options()

app = Flask(__name__)


@app.route("/")
def index():
    with open("./index.html", "r") as val:
        res = val.read()
    return res


@app.route("/<input>")
def analize(input):
    with open("./equation.html", "r") as val:
        res = val.read()
    res = res.replace("%equation%", input)
    explanation = stream_graph_updates(input)[0]
    res = res.replace("%explanation%", explanation)
    return res

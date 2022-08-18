# You Need To Do Something That You Can See flag In Webpage

from flask import Flask, request, render_template_string
import sys

app = Flask(__name__)


@app.route("/welcome")
def handle():
    flag = "S3cr3t T3xt"
    name = request.args.get("name")
    s = """<form><input type="text" name="name"><input type="submit" value="ok"></form>"""
    if name:
        return render_template_string(s + "<br>Hello " + name)
    else:
        return s


@app.route("/")
def main():
    return "Available Routes : ['/welcome']"


if __name__ == "__main__":
    app.run("127.0.0.1", 8080)

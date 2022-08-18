# Just Do A Simple PenTest :)

from flask import Flask,request
from markupsafe import escape

app = Flask(__name__)

@app.route("/welcome")
def handle():
    name = request.args.get("name")
    s = """<form><input type="text" name="name"><input type="submit" value="ok"></form>"""
    if name:
        if escape(name) != name:
            s += "<br>Seems You Did It Bro :))"
        return s + "<br>" + "Hello " + name
    else:
        return s

@app.route("/")
def main():
    return "Available Routes : ['/welcome']"

if __name__ == "__main__":
    app.run("127.0.0.1",8080)
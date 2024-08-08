import secrets

from flask import Flask, render_template, request, session

from api.fetch import fetch_2fa_data
from match.interface import MatchInterface

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404


# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


@app.route("/match", methods=["POST"])
def match():
    api_data = fetch_2fa_data()
    filename = session.get("filename")
    if not filename:
        return "No file uploaded", 400
    matcher = MatchInterface(api_data, filename)
    matched_items = matcher.match()

    return render_template("matches.html", matched_items=matched_items)


@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        f = request.files["file"]
        f.save(f.filename)
        session["filename"] = f.filename
        return render_template("acknowledgement.html", name=f.filename)


if __name__ == "__main__":
    app.run(debug=True)

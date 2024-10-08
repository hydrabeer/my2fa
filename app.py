"""The main entry point for the Flask application. Runs a local web server."""

import secrets

from flask import Flask, render_template, request, session
from werkzeug.utils import secure_filename

from api.fetch import fetch_2fa_data
from match.interface import MatchInterface

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.errorhandler(400)
def bad_request_error(error) -> tuple[str, int]:
    """https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400"""
    return render_template("400.html"), 400


@app.errorhandler(404)
def not_found_error(error) -> tuple[str, int]:
    """https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404"""
    return render_template("404.html"), 404


@app.errorhandler(405)
def method_not_allowed_error(error) -> tuple[str, int]:
    """https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/405"""
    return render_template("405.html"), 405


@app.errorhandler(500)
def internal_error(error) -> tuple[str, int]:
    """https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500"""
    return render_template("500.html"), 500


@app.route("/success", methods=["POST"])
def success() -> str | tuple[str, int]:
    """Display a file upload success page. If no file was uploaded, call the 400 bad
    request error handler.
    """
    f = request.files["file"]
    filename = secure_filename(f.filename)
    if not filename:
        return bad_request_error(400)
    f.save(filename)
    session["filename"] = filename
    return render_template("acknowledgement.html", name=f.filename)


@app.route("/match", methods=["POST"])
def match() -> str:
    """Call the 2FA API fetch function and the matcher and display the matches page."""
    api_data = fetch_2fa_data()
    filename = session.get("filename")
    matcher = MatchInterface(api_data, filename)
    matched_items = matcher.match()
    return render_template("matches.html", matched_items=matched_items)


if __name__ == "__main__":
    app.run(debug=False)

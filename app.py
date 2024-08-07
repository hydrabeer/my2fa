from flask import Flask, render_template

from api.fetch import fetch_2fa_data
from match.interface import MatchInterface

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/match", methods=["POST"])
def match():
    api_data = fetch_2fa_data()
    matcher = MatchInterface(api_data, "bitwarden_export.json")
    matched_items = matcher.match()

    return render_template("index.html", matched_items=matched_items)


if __name__ == "__main__":
    app.run(debug=True)

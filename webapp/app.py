# Packages
from flask import render_template

# Local
from canonicalwebteam.flask_base.app import FlaskBase


app = FlaskBase(
    __name__,
    "multipass.run",
    template_folder="../templates",
    static_folder="../static",
    template_404="404.html",
    template_500="500.html",
)


@app.route("/")
def index():
    return render_template("index.html")

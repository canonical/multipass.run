# Packages
import os
from flask import render_template, request, json, redirect
import talisker.requests

# Local
from canonicalwebteam.flask_base.app import FlaskBase
from canonicalwebteam.discourse_docs import (
    DiscourseAPI,
    DiscourseDocs,
    DocParser,
)

CAPTCHA_API_KEY = os.getenv(
    "CAPTCHA_API_KEY", "6LfYBloUAAAAAINm0KzbEv6TP0boLsTEzpdrB8if"
)

app = FlaskBase(
    __name__,
    "multipass.run",
    template_folder="../templates",
    static_folder="../static",
    template_404="404.html",
    template_500="500.html",
)


# Template context
@app.context_processor
def context():
    return {
        "CAPTCHA_API_KEY": CAPTCHA_API_KEY,
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download/<regex('windows|macos'):osname>")
def osredirect(osname):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_path = os.path.join(SITE_ROOT, "../static/latest-release.json")
    release = json.load(open(json_path))
    return redirect(release["installer_urls"][osname], code=302)


@app.after_request
def no_cache(response):
    if request.path == "/static/latest-release.json":
        response.cache_control.max_age = None
        response.cache_control.no_store = True
        response.cache_control.public = False

    return response


url_prefix = "/docs"
server_docs_parser = DocParser(
    api=DiscourseAPI(
        base_url="https://discourse.ubuntu.com/",
        session=talisker.requests.get_session(),
    ),
    category_id=24,
    index_topic_id=8294,
    url_prefix=url_prefix,
)
server_docs = DiscourseDocs(
    parser=server_docs_parser,
    document_template="/docs/document.html",
    url_prefix=url_prefix,
)

server_docs.init_app(app)

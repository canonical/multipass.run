# Packages
import os
from flask import render_template, request, json, redirect, make_response
import talisker.requests

# Local
from canonicalwebteam.flask_base.app import FlaskBase
from canonicalwebteam.discourse import (
    DiscourseAPI,
    Docs,
    DocParser,
)
from canonicalwebteam.search import build_search_view


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

session = talisker.requests.get_session()


# Template context
@app.context_processor
def context():
    return {
        "CAPTCHA_API_KEY": CAPTCHA_API_KEY,
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/install")
def install():
    return render_template("install.html")


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
main_docs = Docs(
    parser=DocParser(
        api=DiscourseAPI(
            base_url="https://discourse.ubuntu.com/", session=session
        ),
        index_topic_id=8294,
        url_prefix="/docs",
    ),
    document_template="docs/document.html",
    url_prefix="/docs",
    blueprint_name="main_docs",
)
main_docs.init_app(app)


app.add_url_rule(
    "/docs/search",
    "docs-search",
    build_search_view(
        app=app,
        session=session,
        site="multipass.run/docs",
        template_path="docs/search.html",
    ),
)


@app.route("/sitemap.xml")
def sitemap_index():
    xml_sitemap = render_template("sitemap/sitemap-index.xml")
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response


@app.route("/sitemap-links.xml")
def sitemap_links():
    xml_sitemap = render_template("sitemap/sitemap-links.xml")
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response

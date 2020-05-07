from flask import render_template, request, redirect, url_for
from . import main
from ..news_request_handler import NewsRequest
# from ..models import Review
sources = NewsRequest.get_sources

@main.route("/")
def index():
    return render_template("index.html")
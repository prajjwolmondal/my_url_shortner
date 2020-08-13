# -*- coding: utf-8 -*-
from flask import (
    abort,
    Blueprint,
    current_app,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)

from my_url_shortner.main.models import UrlList
from my_url_shortner.main.forms import UrlForm

from random import randint

import re

blueprint = Blueprint("main", __name__, static_folder="../static")

def shortenURL(url: str) -> dict:
    current_app.logger.info(f"url passed in - {url}")
    url_key = ''
    url_without_special_chars = re.sub('(^(https|http)|\W+)', '', url)
    for i in range(0, 6):
        url_key += url_without_special_chars[randint(0, len(url_without_special_chars)-1)]
    UrlList.create(
        short_code=url_key.upper(),
        full_url=url
    )
    return {'original_url': url, 'key': url_key.upper()}

@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    form = UrlForm(request.form)
    current_app.logger.info("Hello from the home page!")
    current_app.logger.info(f"request method - {request.method}")
    if request.method == "POST" and form.validate_on_submit():
        current_app.logger.info(f"url in form- {form.url.data}")
        urlKey = shortenURL(form.url.data)['key']
        return redirect(url_for("main.show_success_page", urlKey=urlKey))
    return render_template("public/home.html", form=form)
    
@blueprint.route("/success", methods=["GET"])
def show_success_page():
    current_app.logger.info(request.args.get('shortenURL'))
    return render_template("public/post_shorten.html", keys=request.args.get('urlKey'))

@blueprint.route('/getAllUrls')
def getAllUrls():
    urls = UrlList.query.all()
    url_list = []
    for url in urls:
        url_list.append(url.convert_to_dict())
    return jsonify(url_list)

@blueprint.route('/url/<short_code>')
def redirectToFullUrl(short_code):
    url = UrlList.query.get(short_code)
    if url is None:
        abort(404) 
    return redirect(url.convert_to_dict()['full_url'])
# -*- coding: utf-8 -*-
from flask import (
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

from random import randint

import re

blueprint = Blueprint("main", __name__, static_folder="../static")

@blueprint.route('/shortenurl', methods=['POST'])
def shortenURL():
    url_key = ''
    url = request.args.get('url')
    url_without_special_chars = re.sub('(^(https|http)|\W+)', '', url)
    for i in range(0, 6):
        url_key += url_without_special_chars[randint(0, len(url_without_special_chars)-1)]
    UrlList.create(
        short_code=url_key.upper(),
        full_url=url
    )
    return jsonify({'original_url': url, 'key': url_key.upper(), 'url_without_special_chars': url_without_special_chars})

@blueprint.route('/getAllUrls')
def getAllUrls():
    urls = UrlList.query.all()
    url_list = []
    for url in urls:
        url_list.append(url.convert_to_dict())
    return jsonify(url_list)

@blueprint.route('/url/<short_code>')
def getFullUrl(short_code):
    url = UrlList.query.get(short_code)
    return jsonify(url.convert_to_dict())
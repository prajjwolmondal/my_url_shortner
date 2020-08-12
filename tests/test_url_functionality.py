# -*- coding: utf-8 -*-

from flask import url_for, request

from my_url_shortner.main.models import UrlList

from .factories import UrlFactory


class TestUrlFunctionality:
    """URL fetching, and adding."""

    def test_valid_shortcode_returns_valid_status_code(self, testapp):
        res = testapp.get('/url/ULOTIG')
        assert res.status_code == 302

    # TODO: Fix test
    def test_valid_shortcode_returns_valid_url(self, testapp):
        res = testapp.get('/url/ULOTIG').follow()
        print(f"request_path: {request.path}")
        assert request.path== "https://github.com/prajjwolmondal/"

    def test_get_all_urls_returns_valid_status_code(self, testapp):
        res = testapp.get('/getAllUrls')
        assert res.status_code == 200

    def test_get_all_urls_returns_more_than_one_url(self, testapp):
        res = testapp.get('/getAllUrls') 
        assert len(res.json) > 1

    # TODO: Fix test
    def test_url_is_added_to_db(self, testapp):
        urls = UrlList.query.all()
        print(f"urls: {urls}")
        db_length_before = len(urls)
        print(f"db_length_before: {db_length_before}")
        res = testapp.get(url_for("main.home")).follow()
        print(f"res: {res.forms}")
        assert False
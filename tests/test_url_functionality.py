# -*- coding: utf-8 -*-

from flask import url_for

from .factories import UrlFactory


class TestUrlFunctionality:
    """URL fetching, and adding."""

    def test_valid_shortcode_returns_valid_status_code(self, testapp):
        res = testapp.get('/ULOTIG')
        assert res.status_code == 200

    def test_valid_shortcode_returns_valid_url(self, testapp):
        res = testapp.get('/ULOTIG')
        assert res.json['full_url'] == "https://github.com/prajjwolmondal/"

    def test_get_all_urls_returns_valid_status_code(self, testapp):
        res = testapp.get('/getAllUrls')
        assert res.status_code == 200

    def test_get_all_urls_returns_more_than_one_url(self, testapp):
        res = testapp.get('/getAllUrls') 
        assert len(res.json) > 1

    
# -*- coding: utf-8 -*-

from flask import url_for, request

from my_url_shortner.main.models import UrlList

from .factories import UrlFactory


class TestUrlFunctionality:
    """URL fetching, and adding."""

    def test_valid_shortcode_returns_valid_status_code(self, testapp):
        """You should get redirected when hitting a url shortcode"""
        res = testapp.get('/url/ULOTIG')
        assert res.status_code == 302

    def test_invalid_shortcode_returns_invalid_status_code(self, testapp):
        """You should get 404 error when hitting an invalid url shortcode"""
        res = testapp.get('/url/CIRCLES', expect_errors=True)
        assert res.status_code == 404

    def test_valid_shortcode_returns_valid_url(self, testapp):
        """You should get redirected to the correct URL when hitting a url shortcode"""
        res = testapp.get('/url/ULOTIG', status=[302])
        assert res.headers['Location'] == "https://github.com/prajjwolmondal/"

    def test_get_all_urls_returns_valid_status_code(self, testapp):
        """200 status code returned when fetching all URLs"""
        res = testapp.get('/getAllUrls')
        assert res.status_code == 200

    def test_get_all_urls_returns_more_than_one_url(self, testapp):
        """More than 1 URL returned when fetching all URLs"""
        res = testapp.get('/getAllUrls') 
        assert len(res.json) > 1

    def test_url_is_added_to_db(self, testapp):
        """Submitting a new URL via the homepage form, adds it to the DB"""
        old_numb_of_urls = len(UrlList.query.all())
        res = testapp.get('/')
        search_form = res.forms['urlForm']
        search_form['url'] = "https://docs.pylonsproject.org/projects/webtest/en/latest/api.html"
        res = search_form.submit().follow()
        assert len(UrlList.query.all()) == old_numb_of_urls + 1

        
# -*- coding: utf-8 -*-

from my_url_shortner.main.models import UrlList


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

    def test_url_is_added_to_db_when_not_logged_in(self, testapp):
        """Submitting a new URL via the homepage form, adds it to the DB"""
        old_numb_of_urls = len(UrlList.query.all())
        res = testapp.get('/')
        search_form = res.forms['urlForm']
        search_form['url'] = "https://docs.pylonsproject.org/projects/webtest/en/latest/api.html"
        res = search_form.submit().follow()
        assert len(UrlList.query.all()) == old_numb_of_urls + 1

        
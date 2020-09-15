# -*- coding: utf-8 -*-

from flask import url_for, session, request


class TestUserFunctionality:
    """Testing user specific functionality"""

    def login(self, client):
        return client.post("/users/login", dict(
            username = "prajjwolm",
            password = "test12"
        ))

    def test_get_users_urls_works(self, testapp):
        """200 status code returned when fetching all URLs for an user"""

        rv = self.login(testapp)
        res = testapp.get('/users/user_urls')
        assert res.status_code == 200

    def test_get_user_urls_returns_data(self, testapp):
        """Actual data returned when fetching all URLs for an user"""
        rv = self.login(testapp)
        res = testapp.get('/users/user_urls')
        assert len(res.json) >= 1


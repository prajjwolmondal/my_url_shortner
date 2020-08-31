# -*- coding: utf-8 -*-

from flask import url_for, session, request


class TestUserFunctionality:
    """Testing user specific functionality"""

    def test_get_users_urls_works(self, testapp):
        """200 status code returned when fetching all URLs for an user"""

        session['user_id'] = "52d9b126-b193-45d7-8353-e20ceaec"
        print(f"session: {session.keys()}")
        res = testapp.get('/users/user_urls')
        assert res.status_code == 200

    # def test_get_user_urls_returns_data(self, testapp):
    #     """Actual data returned when fetching all URLs for an user"""

    #     assert False


# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import logging

import pytest
from webtest import TestApp

from my_url_shortner.app import create_app
from my_url_shortner.database import db as _db

from .factories import UserFactory


@pytest.fixture
def app():
    """Create application for the tests."""
    _app = create_app("tests.settings")
    _app.logger.setLevel(logging.CRITICAL)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def testapp(app):
    """Create Webtest app."""
    return TestApp(app)


@pytest.fixture
def db(app):
    """Create database for the tests."""
    _db.app = app
    with app.app_context():
        _db.session.remove()
        # _db.drop_all()
        _db.create_all()

    yield _db

    print("Running after yield")
    _db.session.remove()
    # _db.drop_all()

    ## This dispose() call is needed to avoid the DB locking
    ## between tests.
    ## Thanks to:
    ## http://stackoverflow.com/a/18293157/2066849
    _db.get_engine(_db.app).dispose()


@pytest.fixture
def user(db):
    """Create user for the tests."""
    user = UserFactory()
    print(f"userfixture: {user}")
    db.session.commit()
    return user

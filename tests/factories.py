# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import PostGenerationMethodCall, Sequence, LazyAttribute
from factory.alchemy import SQLAlchemyModelFactory

import datetime

from my_url_shortner.database import db
from my_url_shortner.user.models import User


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    """User factory."""

    username = Sequence(lambda n: f"user{n}")
    email = Sequence(lambda n: f"user{n}@example.com")
    password = PostGenerationMethodCall("set_password", "example")
    active = True

    class Meta:
        """Factory configuration."""

        model = User

class UrlFactory(BaseFactory):
    """URL factory."""

    short_code = 'ULOTIG'
    full_url = 'https://github.com/prajjwolmondal/'
    created_at = LazyAttribute(datetime.datetime.now)
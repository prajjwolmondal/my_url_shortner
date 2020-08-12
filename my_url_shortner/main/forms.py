# -*- coding: utf-8 -*-
"""Main form."""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

from my_url_shortner.user.models import User


class UrlForm(FlaskForm):
    """Form to submit requests to shorten URL."""

    url = StringField("Full URL", validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(UrlForm, self).__init__(*args, **kwargs)

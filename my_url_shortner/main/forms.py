# -*- coding: utf-8 -*-
"""Main form."""
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import SearchField

from my_url_shortner.user.models import User


class UrlForm(FlaskForm):
    """Form to submit requests to shorten URL."""

    url = SearchField("Full URL", validators=[DataRequired(), Length(max=120)])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(UrlForm, self).__init__(*args, **kwargs)

# -*- coding: utf-8 -*-
"""User forms."""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from .models import User

import re

class RegisterForm(FlaskForm):
    """Register form."""

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=5, max=25)]
    )
    email = StringField(
        "Email", validators=[DataRequired(), Email(), Length(min=6, max=40)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        "Verify password",
        [DataRequired(), EqualTo("password", message="Passwords must match")],
    )

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        if not self.validate_user_name():
            return False
        if not self.validate_user_email():
            return False
        if not self.validate_pwd():
            return False
        return True

    def validate_user_name(self):
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append(f"{user.username} has already been registered")
            return False
        return True
    
    def validate_user_email(self):
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append(f"{user.email} has already been registered")
            return False
        return True

    def validate_pwd(self):
        """Passwords need to be at least 8 chars long, have a letter, number and special char"""

        # Thanks to https://stackoverflow.com/a/2990682 for the regex
        if re.fullmatch(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$',
                        self.password.data):
            return True
        else:
            self.password.errors.append(f"Your password doesn't match the requirements.")
            return False
        

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        # TODO: Replace these errors to be more generic so a malicious user doesn't know which one is correct.
        self.user = User.query.filter_by(username=self.username.data).first()
        if not self.user:
            self.username.errors.append("Unknown username")
            return False

        if not self.user.check_password(self.password.data):
            self.password.errors.append("Invalid password")
            return False

        return True
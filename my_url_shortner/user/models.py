# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin

from my_url_shortner.database import (
    Column,
    Model,
    db,
    reference_col,
    relationship,
)
from my_url_shortner.extensions import bcrypt


class User(UserMixin, Model):
    """A user of the app."""

    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = Column(db.String(40), unique=True, nullable=False)
    email = Column(db.String(60), unique=True, nullable=False)
    password = Column(db.LargeBinary(128), nullable=False)   # The hashed password
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(45), nullable=True)
    active = Column(db.Boolean(), nullable=False, default=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, username, email, password=None, **kwargs):
        """Create instance."""
        super().__init__(username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    def get_id(self):
        return self.username

    @property
    def full_name(self):
        """Full user name."""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<User({self.username!r})>"

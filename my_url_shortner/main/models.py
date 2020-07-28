# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from my_url_shortner.database import (
    Column,
    Model,
    db,
)


class UrlList(Model):
    """Main table containing the short URL <-> long URL map"""

    __tablename__ = "UrlList"
    short_code = Column(db.String(6), unique=True, nullable=False, primary_key=True)
    full_url = Column(db.String(80), nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __repr__(self) -> str:
        """Represent instance as a unique string."""
        return f"<Url_key({self.short_code})>"

    def convert_to_dict(self) -> dict:
        return {'short_code': self.short_code, 'full_url': self.full_url}
# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from my_url_shortner.database import (
    Column,
    Model,
    db,
)


class UrlList(Model):
    """Main table containing the info needed for the URLs"""

    __tablename__ = "urllist"
    short_code = Column(db.String(6), unique=True, nullable=False, primary_key=True)
    full_url = Column(db.String(120), nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    created_by = Column(db.String(32), nullable=False)

    def __repr__(self) -> str:
        """Represent instance as a unique string."""
        return f"<Url_key({self.short_code})>"

    def convert_to_dict(self) -> dict:
        return {'short_code': self.short_code, 'full_url': self.full_url, 'created_at': self.created_at, 'created_by': self.created_by}
# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, login_user, logout_user

from my_url_shortner.extensions import login_manager
from my_url_shortner.user.models import User
from my_url_shortner.utils import flash_errors

blueprint = Blueprint("public", __name__, static_folder="../static")


@login_manager.user_loader
def load_user(user_name):
    """Load user by ID."""
    current_app.logger.info(f"user_name: {user_name}")
    return User.query.filter_by(username=user_name).first()


@blueprint.route("/logout/")
@login_required
def logout():
    """Logout."""
    logout_user()
    flash("You are logged out.", "info")
    return redirect(url_for("main.home"))


@blueprint.route("/about/")
def about():
    """About page."""
    return render_template("public/about.html")

# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
from flask_login import login_user

from .forms import LoginForm, RegisterForm
from .models import User
from my_url_shortner.utils import flash_errors

blueprint = Blueprint("user", __name__, url_prefix="/users", static_folder="../static")


@blueprint.route("/signinpage")
def signinPage():
    login_form = LoginForm()
    register_form = RegisterForm()
    return render_template("public/register.html", loginForm=login_form, registerForm=register_form)

@blueprint.route("/register/", methods=["POST"])
def register():
    """Register new user."""
    register_form = RegisterForm(request.form)
    login_form = LoginForm()
    if register_form.validate_on_submit():
        User.create(
            username=register_form.username.data,
            email=register_form.email.data,
            password=register_form.password.data,
            active=True,
        )
        flash("Thank you for registering. You can now log in.", "success")
        return redirect(url_for("user.signinPage"))
    else:
        flash_errors(register_form)
    return render_template("public/register.html", loginForm=login_form, registerForm=register_form)

@blueprint.route("/login", methods=["POST"])
def login():
    register_form = RegisterForm()
    login_form = LoginForm(request.form)
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        current_app.logger.info(f"username: {login_form.username.data}")
        current_app.logger.info(f"user: {user}")
        login_user(user)
        flash("You are logged in.", "success")
        return redirect(url_for("main.home"))
    else:
        flash_errors(login_form)
    return render_template("public/register.html", loginForm=login_form, registerForm=register_form)
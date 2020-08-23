# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, current_app, flash, jsonify, redirect, render_template, request, session, url_for
from flask_login import login_user, login_required

from .forms import LoginForm, RegisterForm
from .models import User

from my_url_shortner.main.models import UrlList
from my_url_shortner.utils import flash_errors

from uuid import uuid4

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
        generated_user_id = uuid4()
        User.create(
            username=register_form.username.data,
            email=register_form.email.data,
            password=register_form.password.data,
            active=True,
            user_id = generated_user_id,
        )
        session['user_id'] = generated_user_id
        login_user(User.query.filter_by(username=register_form.username.data).first())
        flash("Thank you for registering. You have been logged in.", "success")
        return redirect(url_for("main.home"))
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
        session['user_id'] = user.user_id
        login_user(user)
        flash("You are logged in.", "success")
        return redirect(url_for("main.home"))
    else:
        flash_errors(login_form)
    return render_template("public/register.html", loginForm=login_form, registerForm=register_form)

def getAllUrlsForLoggedInUser():
    """Get all URLs associated with current logged in user"""
    user_id = session['user_id']
    urls = UrlList.query.filter_by(created_by=user_id).all()
    url_list = []
    for url in urls:
        url_list.append(url.convert_to_dict())
    return url_list

@blueprint.route("/user_profile")
@login_required
def user_profile():
    user_urls = getAllUrlsForLoggedInUser()
    current_app.logger.info(f"user_urls: {user_urls}")
    if len(user_urls) > 0:
        return render_template("users/user_profile.html", user_urls=user_urls)
    else:
        return render_template("users/user_profile.html")
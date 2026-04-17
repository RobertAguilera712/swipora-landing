from flask import render_template, url_for, redirect, Blueprint, flash, request

page = Blueprint("page", __name__, template_folder="../templates/page")

@page.route("/", methods=["GET"])
def home():
    return render_template("index.jinja2")
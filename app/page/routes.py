from flask import render_template, url_for, redirect, Blueprint, flash, request

page = Blueprint("page", __name__, template_folder="../templates/page")

@page.route("/", methods=["GET"])
def index():
    return render_template("index.jinja2", title="Swipora | Aprende inglés de manera inteligente")

@page.route("/privacy-policy/", methods=["GET"])
def privacy():
    return render_template("privacy-policy.jinja2", title="Swipora | Política de privacidad")

@page.route("/terms-of-service/", methods=["GET"])
def terms():
    return render_template("terms-of-service.jinja2", title="Swipora | Términos de servicio")

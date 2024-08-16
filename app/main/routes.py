from flask import Blueprint, render_template
from flask_login import login_required

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    return render_template("home.html", title="Home")


@main_bp.route("/authenticated_page")
@login_required
def authenticated_page():
    return render_template("authenticated_page.html")

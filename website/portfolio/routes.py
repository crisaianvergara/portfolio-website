from flask import Blueprint, render_template


portfolios = Blueprint("portfolios", __name__)


@portfolios.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", title="Portfolio")

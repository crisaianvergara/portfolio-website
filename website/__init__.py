from flask import Flask


def create_app():
    app = Flask(__name__)

    from website.main.routes import main
    from website.portfolio.routes import portfolios

    app.register_blueprint(main)
    app.register_blueprint(portfolios)

    return app

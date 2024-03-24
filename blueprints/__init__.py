from flask import Blueprint

from .views import (
    login,
    callback,
    tracks,
)

bp = Blueprint(
    "blueprints",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path='/app/blueprints/static/'
)

bp.add_url_rule(
    rule="/",
    view_func=login,
    endpoint='login',
    methods=['GET'],
)
bp.add_url_rule(
    rule="/callback",
    view_func=callback,
    endpoint='callback',
    methods=["GET"]
)
bp.add_url_rule(
    rule="/tracks",
    view_func=tracks,  # type: ignore
    endpoint='tracks',
    methods=["GET"]
)


def init_app(app):  # type: ignore
    app.register_blueprint(bp)

from flask import Blueprint

bp = Blueprint('users', __name__, url_prefix='/auth')


@bp.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

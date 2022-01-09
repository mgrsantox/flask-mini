from flask import Blueprint

# Main Page blueprint
bp = Blueprint('main', __name__, url_prefix='/')


# Main page route

@bp.route("/")
def index():
    return "<h1 style='color:blue'>Flask Mini Project</h1>Documentation link <a href='https://documenter.getpostman.com/view/13592153/UVXesJ2w'>Click Here</a>"

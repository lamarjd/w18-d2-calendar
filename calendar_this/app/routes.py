from flask import (Blueprint, render_template)


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route("/")
def main():
    # render the main.html using render_template
    return render_template('main.html')
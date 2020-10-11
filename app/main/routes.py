from app.main import bp
from flask_login import login_required
from flask import render_template

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')

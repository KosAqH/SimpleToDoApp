from flask import Blueprint, render_template
from flask_login import login_required
from . import db

main = Blueprint('main', __name__)

@login_required
@main.route('/')
def index():
    return render_template('index.html')
from flask import render_template, Blueprint
from flask_login import login_required, current_user
home = Blueprint('home', __name__)

@home.route('/', methods=['POST', 'GET'])
def home_page():
    return render_template('home_page.html')
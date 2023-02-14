from flask import render_template,session, make_response
from flask_login import login_required, current_user

from . import main

@main.route('/index')
@login_required
def index():
    print(session.get('test', 'ok'))
    temp = render_template('main/index.html')
    response = make_response(temp)

    response.set_cookie("name", "python")

    return response
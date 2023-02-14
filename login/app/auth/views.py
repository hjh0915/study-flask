from flask import render_template, request, redirect, session
from flask_login import login_required, logout_user, login_user
from . import auth
from ..models import User

@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('pwd')
        
        # 验证User
        u = User.query.filter_by(username=username).first()
        if u == None:
            return render_template('auth/login.html')
        
        if u.verify_password(password):
            login_user(u)
            session['test'] = 'abc'
            return redirect('/main/index')
        else:
            return render_template('auth/login.html')
    

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('test')
    return redirect('/auth/login')
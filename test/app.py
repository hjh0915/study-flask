from flask import Flask, render_template, request, redirect

app = Flask(__name__)

users = [
    {'uid': 1001, 'img': '#', 'uname': 'aaa', 'tel': '12345678910'},
    {'uid': 1002, 'img': '#', 'uname': 'bbb', 'tel': ''},
    {'uid': 1003, 'img': '#', 'uname': 'ccc', 'tel': '98765437123'}
]

# 首页跳转至登录页
@app.route('/')
def index():
    return redirect('/login')

# 登录页
@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/result", methods=["POST", "GET"])
def show_user():
    admin = request.form.get("admin")
    return render_template('result.html', users=users, admin=admin)

# 修改用户电话号码
@app.route("/update", methods=['POST','GET'])
def update_users():
    if request.method == 'POST':
        uid = request.form.get('uid')
        img = request.form.get('img')
        uname = request.form.get('uname')
        tel = request.form.get('tel')

        for user in users:
            if user['uname'] == uname:
                user['uid'] = uid 
                user['img'] = img
                user['uname'] = uname
                user['tel'] = tel
                return redirect('/result')
        return 'no found'
    else:
        uname = request.args.get('uname')
        for user in users:
            if user['uname'] == uname:
                return render_template('update.html', user=user)
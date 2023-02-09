项目结构分层
==========
app.py
templates下存放.html文件
static下存放css,js等文件

前后端交互
=========
@app.route('/')

POST
====
提交

GET
===
获取

执行
====
> $ export FLASK_APP=app.py
> $ flask run

> $ flask --app app.py --debug run
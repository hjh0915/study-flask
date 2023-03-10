from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')
 
@app.route('/result', methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template('result.html', result=result)
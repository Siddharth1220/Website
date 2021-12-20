from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gb')
def gb():
    return render_template('gb.html')

@app.route('/gt')
def gt():
    return render_template('gt.html')

@app.route('/ach')
def ach():
    return render_template('ach.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
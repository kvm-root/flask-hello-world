from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'Kratos' and password == 'KingV000n':
            return redirect('http://www.welpeckroot.cn')
        else:
            return 'Invalid credentials. Please try again.'
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

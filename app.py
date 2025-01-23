import sqlite3
from flask import (
    Flask,
    render_template,
    redirect,
    request,
    url_for
)
connection = sqlite3.connect('users.db')
cursor = connection.cursor()


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def get_main():
    return render_template('base.html')


@app.route('/log', methods=['GET','POST'])
def get_log():
    return render_template('log.html')


@app.route('/home', methods=['GET','POST'])
def get_home():
    return render_template('home.html')



@app.route('/reg', methods=['GET','POST'])
def get_reg():
    if request.method == 'POST':
        login = request.form.get('login', type=str)
        password = request.form.get('password', type=str)
        if login == 'admin' and password == 'admin':
            return redirect(url_for('get_home', login=login, password=password))
        else:
            return "<h1>Ебать ты хуй</h1>"
    return render_template('reg.html')




if __name__ == '__main__':
    app.run(debug=True)
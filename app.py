from flask import (
    Flask,
    render_template,
    redirect,
    request
)
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def get_main():
    return render_template('base.html')


@app.route('/log', methods=['GET','POST'])
def get_log():
    return render_template('log.html')


@app.route('/reg', methods=['GET','POST'])
def get_reg():
    return render_template('reg.html')




if __name__ == '__main__':
    app.run(debug=True)
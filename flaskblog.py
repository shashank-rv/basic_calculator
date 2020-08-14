from flask import Flask,render_template,request
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '9f26b3cb54b5b4da5199c31135907789'


@app.route("/")
def calc():
    return render_template('calc.html',title = 'calculator')

@app.route("/",methods = ['POST'])
def calc1():
    number1 = request.form['number1']
    number2 = request.form['number2']
    return number1+number2


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask,request,render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/forms")
def forms():
    return render_template('forms.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method=='POST':
       a=request.form['fullName']
       b=request.form['age']
       c=request.form['gender']
       return a+" "+b+" "+c
    else:
        return "error"
    


if __name__ == '__main__':
    app.run(debug=True)

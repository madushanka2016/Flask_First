from flask import Flask,request,render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/list")
def list():
    return render_template('list.html')


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

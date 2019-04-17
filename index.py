from flask import Flask, render_template,request,flash
from flask_mysqldb import MySQL
app = Flask(__name__)



# config MqSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#inti MySQL
mysql = MySQL(app)


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
       name=request.form['fullName']
       age=request.form['age']
       gender=request.form['gender']
       userName=request.form['userName']
       pw=request.form['pw']
       # return name+" "+age+" "+gender+" "+pw+" "+userName
       cur =mysql.connection.cursor()

       cur.execute("INSERT INTO details(name) VALUES(%s)",(name))
       # cur.close()
       return render_template("forms.html")
    else:
        return "error"
    


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template,request,flash
from flask_mysqldb import MySQL
from flask_mail import Mail, Message
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
       	name=request.form['name']
       	email=request.form['email']
       	gender=request.form['gender']
       	userName=request.form['userName']
       	pw=request.form['pw']

        cur =mysql.connection.cursor()
        cur.execute("INSERT INTO details(name,email,gender,userName,pw) VALUES(%s , %s , %s , %s , %s)",(name,email,gender,userName,pw))
        cur.close()


        ### send email

        #config
        app.config['MAIL_SERVER']='smtp.gmail.com'
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USERNAME'] = 'pasanmalinda10@gmail.com'
        app.config['MAIL_PASSWORD'] = '0773697320'
        app.config['MAIL_USE_TLS'] = False
        app.config['MAIL_USE_SSL'] = True
        mail = Mail(app)

        msg = Message('Vertify Email', sender = 'pasanmalinda10@gmail.com', recipients = [email])
        msg.body = "your vertify code is ****"
        mail.send(msg)

        return render_template("forms.html")
    else:
        return "error"


if __name__ == '__main__':
    app.run(debug=True)

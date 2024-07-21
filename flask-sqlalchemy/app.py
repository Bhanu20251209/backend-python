from flask import Flask,request,redirect
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
db = SQLAlchemy(app)
app.app_context().push()
class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))

def __init__(self, name, city, addr,pin):
   self.name = name
   self.city = city
   self.addr = addr
   self.pin = pin

@app.route('/', methods=['GET','POST'])
def home():
  if   request.method=='GET':
     return render_template('index.html')
  elif request.method=='POST':
     n=request.form['name']
     c=request.form['city']
     a=request.form['addr']
     p=request.form['pin']
     p1=students(name=n,city=c,addr=a,pin=p)
     db.session.add(p1)
     db.session.commit()
     profile=students.query.all()
     return render_template('students.html',profile=profile)
  
if __name__=='__main__':
   app.run(debug=True)
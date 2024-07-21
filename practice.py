from flask import Flask 
from flask import render_template,redirect,url_for
from flask import request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    if request.method=='GET':
        return render_template('hello.html')
    elif request.method=='POST':
        a=request.form['your_name']
        return render_template('display.html',display_name=a)
    else:
        return 'error'
    
        
 
 
if __name__=='__main__':
    app.debug=True
    app.run()
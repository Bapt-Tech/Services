from flask import Flask, render_template
#from ModSer import ModLogSer
import time
import os
app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=False, host='192.168.1.22', port=5000)


@app.route('/')
def index():
    return render_template("indexBugged.html")

@app.route('/Login_Service')
def Login_Service():
    return render_template('index_Login_Service.html')

@app.route('/APropos')
def APropos():
    return render_template('indexAPropos.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('Hello_Name.html', name=name)



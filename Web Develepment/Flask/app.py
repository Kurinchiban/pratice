from flask import Flask,render_template
from markupsafe import escape

app=Flask(__name__,template_folder="template")

@app.route('/')
def hellow():
    return render_template ('index.html')

@app.route('/user/<username>')
def user(username):
    return "Welcome User : %s"%escape(username)

if __name__=="__main__":
    app.run(debug=True)

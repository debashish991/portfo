#$env:FLASK_APP = "server.py" run this cmd on powershell
#then cmd flask run
#to turn on debug mode\
# $env:FLASK_ENV = "development"
# $env:FLASK_DEBUG = "1"
# flask run

# server.py

from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    #return "<p>Hello, Debashish!</p>"  # Correcting the return statement and ensuring proper termination
    return render_template('index.html') # alternative of line 17. Here with line 18 the webpage is directly getting informaation from server.

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def work():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html') Note: There is a dynamic way of writing the code. from line 20 to 29 the dynamic code is written in line 32.

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["email"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["email"]
        csv_writer = csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. Try again'
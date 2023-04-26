from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)  # hence, exported as 'app'

@app.route("/")
def index():
    return render_template('index.html')  # flask automatically looks for files in the 'template' folder

@app.route("/<string:page_name>")
def my_home(page_name):
    return render_template(page_name)  # flask automatically looks for files in the 'template' folder

def write_to_file(data):
    with open('./database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('./database.csv', 'a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        fieldnames = ['email', 'subject', 'message']
        csv_writer = csv.DictWriter(database, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if database.tell() == 0:  # if cursor == 0, meaning file is empty
            csv_writer.writeheader()
        csv_writer.writerow({'email':email, 'subject':subject, 'message':message})

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'


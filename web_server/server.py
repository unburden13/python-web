from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/<string:page_name>")
def my_home(page_name):
    return render_template(page_name)  # flask automatically looks for files in the 'template' folder

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'

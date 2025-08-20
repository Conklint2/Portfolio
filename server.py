import csv

from flask import Flask, request, render_template, redirect, json
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name + '.html')

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([data['email'], data['subject'], data['message']])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            with open('database.txt', 'a') as file:
                file.write(str(data) + '\n')
                write_to_csv(data)
            return redirect('./thankyou')
        except:
            return 'Could not submit form'
    return render_template('./contact.html')

from flask import Flask, render_template,request
import csv

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/<string:page_name>")
def name_page(page_name=None):
    return render_template(page_name)
def write_the_file(data):
    with open('contact_data.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{name},{email},{subject},{message}')
def write_csv_file(data):
    with open('database.csv', newline='', mode='a') as database2:
            name = data['name']
            email = data['email']
            subject = data['subject']
            message = data['message']
            csv_file = csv.writer(database2,delimiter='|', quotechar='"',quoting=csv.QUOTE_NONE)
            csv_file.writerow([name,email,subject,message])
@app.route('/submit_info', methods=['POST', 'GET'])
def submit_info():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_csv_file(data)
            return 'thank you'
        except:
            return'did not save it'
    else:
        return 'something went wrong!'
        
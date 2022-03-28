from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# localhost:5000/
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    if request.form['txt_name'] == 'Boris' and request.form['txt_password'] == '1234':
        return render_template('borisfb.html')
    return render_template('error.html')

app.run()
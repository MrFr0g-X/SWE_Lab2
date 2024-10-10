from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    age = request.form['age']
    
    message = f'Hello {name}, you are {age} years old!'
    return render_template('results.html', message=message)
if __name__ == '__main__':
    app.run(debug=True)

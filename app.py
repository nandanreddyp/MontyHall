print('welcome to monty hall')
from flask import Flask, render_template, redirect

app = Flask('__main__', template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/play', methods=['GET', 'POST'])
def play():
    pass
    return render_template('first.html')

if __name__=='__main__':
    app.run(debug=True)
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    message = request.form['message']
    return f'Teşekkürler! Gönderdiğiniz mesaj: {message}'

if __name__ == '__main__':
    app.run(debug=True)

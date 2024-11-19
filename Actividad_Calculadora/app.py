from flask import Flask, render_template, request
from Comparar.Grammar import validate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_string = request.form['input_string']
    # Validar si la expresión es válida según la gramática
    if validate(input_string):
        result_message = "Cadena válida"
    else:
        result_message = "Cadena no válida"

    return render_template('index.html', result=result_message)

if __name__ == '__main__':
    app.run(debug=True)

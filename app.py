from flask import Flask, render_template, request
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)  # Passa a instância da aplicação

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2 if num2 != 0 else 'Erro: Divisão por zero!'
        except ValueError:
            result = 'Erro: Insira números válidos!'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Para gerar a versão estática
    freezer.freeze()

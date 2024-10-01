from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)  # Passa a instância da aplicação

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Para gerar a versão estática
    freezer.freeze()

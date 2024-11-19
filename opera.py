from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form['nombre']
    # Procesa la información aquí
    return 'Información procesada con éxito'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, redirect, url_for
from flask_session import Session


app = Flask(__name__)
app.config['SECRETKEY'] = 'secretkey'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)


@app.route('/')
def index():
    return render_template('gallery.html')

@app.route('/banderines')
def banderines():
    return render_template('banderines.html')

@app.route('/piniatas')
def piniatas():
    return render_template('piniatas.html')

@app.route('/cajitas')
def cajitas():
    return render_template('cajitas.html')

@app.route('/letras')
def letras():
    return render_template('letras.html')

@app.route('/centros_mesa')
def centros_mesa():
    return render_template('centros_mesa.html')

@app.route('/marcos')
def marcos():
    return render_template('marcos.html')

@app.route('/souvenirs')
def souvenirs():
    return render_template('souvenirs.html')

@app.route('/gigantografias')
def gigantografias():
    return render_template('gigantografias.html')

@app.route('/flores')
def flores():
    return render_template('flores.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
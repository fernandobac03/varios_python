from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/informacion/<string:nombre>/<string:apellido>/<int:edad>')
def informacion(nombre,apellido,edad):

    return render_template('informacion.html',
                           nombre=nombre,
                           apellido=apellido,
                           edad=edad
                           )


# configurando para parámetros opcionales, se agregan rutas adicioanles para los casos
@app.route('/contacto')
@app.route('/contacto/<string:nombre>')
@app.route('/contacto/<string:nombre>/<apellido>')
def contacto(nombre=None, apellido=None):

    return f"""<h1>PÁGINA DE CONTACTO</h1>
                <h3>Tu nombre es: {nombre} {apellido} </h3>
    
           """


# Redireccionando
@app.route('/nosotros')
@app.route('/nosotros/<redireccion>')
def nosotros(redireccion=None):
    if redireccion is not None:
        return redirect(url_for('lenguajes'))
    else:
        return f"""<h1>PÁGINA DE CONTACTO</h1>
                <h3>Se decidió no redireccionar </h3>
           """


@app.route('/lenguajes')
def lenguajes():
    return "<h1>PÁGINA DE LENGUAJES DE PROGRAMACIÓN</h1>"





if __name__ == '__main__':
    app.run(debug=True) #Por que lo que se necesita es que el srevidor de flask, cuando hago cambios se recarga automáticamente

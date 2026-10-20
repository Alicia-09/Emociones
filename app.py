from flask import Flask, render_template,request,flash,url_for,redirect,session

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route('/sesion')
def sesion():
    return render_template("sesion.html")

@app.route('/cerrar_sesion')
def cerrar_sesion():
    session.clear()
    flash('Has cerrado sesión correctamente', 'success')
    return redirect(url_for('inicio'))

if __name__ == "__main__":
    app.run(debug=True)
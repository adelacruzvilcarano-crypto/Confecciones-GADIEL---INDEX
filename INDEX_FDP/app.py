from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index_confecciones_gadiel.html")

@app.route("/productos")
def productos():
    return render_template("productos.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/contactos")
def contactos():
    return render_template("contactos.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        with open("usuarios.txt", "a") as f:
            f.write(f"{usuario},{password}\n")

        return render_template("login.html", mensaje="Usuario guardado")

    return render_template("login.html")


# REGISTRO
@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        with open("usuarios.txt", "a") as f:
            f.write(f"{usuario},{password}\n")

        return render_template("registro.html", mensaje="Usuario registrado")

    return render_template("registro.html")


if __name__ == "__main__":
    app.run(debug=True)
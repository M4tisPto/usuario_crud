from flask import Flask, request, render_template, redirect
from usuarios import Usuario
app = Flask(__name__)

@app.route("/")

def index():
    return "Hola"

@app.route("/usuarios")

def usuarios_lista():
    usuarios = Usuario.get_all()
    print(usuarios)
    return render_template("tabla_usuarios.html", todos_los_usuarios = usuarios)


@app.route("/registrar", methods=["GET"])
def registrar():
    return render_template("registro.html")

@app.route("/actualizar_usuario", methods= ["POST"])
def actualizar_usuario():
    datos = {
        "id" : request.form["id"],
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"]
    }

    Usuario.update_data(datos)
    return redirect("/usuarios")

    # si, mi tabla de base de datos es muy simple xd

if __name__ == "__main__":
    app.run(debug=True)

# this for now
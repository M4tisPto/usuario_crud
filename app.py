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


@app.route("/usuarios/nuevo")
def registrar():
    return render_template("nuevo_usuario.html")

@app.route("/usuarios/borrar/<int:id>")
def borrar_usuario(id):
    datos ={
        "id": id
    }
    Usuario.delete_user(datos)
    return redirect("/usuarios")

@app.route("/registrar_usuario", methods=["POST"])
def registrar_usuario():
    datos = {

        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }

    Usuario.save(datos)
    return redirect("/usuarios")

@app.route("/usuarios/<int:id>")
def ver_usuario(id):
    datos = {
        "id": id
    }
    usuario = Usuario.get_one(datos)
    return render_template("ver_usuario.html", un_usuario = usuario)

@app.route("/usuarios/editar/<int:id>")
def editar_usuario(id):
    datos = {
        "id": id
    }
    usuario = Usuario.get_one(datos)
    return render_template("editar_usuario.html", un_usuario = usuario)

@app.route("/actualizar_usuario", methods=["POST"])
def actualizar_usuario():
    datos = {
        "id": request.form["id"],
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.update_data(datos)
    return redirect("/usuarios")


if __name__ == "__main__":
    app.run(debug=True)
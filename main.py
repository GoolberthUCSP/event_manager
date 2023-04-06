from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

class User:
    def __init__(self, _email, _password, _type):
        self.email = _email
        self.password = _password
        self.type = _type

users = []
users.append(User("admin@gmail.com", "admin", 1))
users.append(User("encargado@gmail.com", "encargado", 2))
users.append(User("colab@gmail.com", "colab", 3))
users.append(User("client@gmail.com", "client", 4))

@app.route("/", methods =["GET", "POST"])
def home():
    if request.method == "POST":
        for user in users:
            if user.email == request.form.get("email") and user.password == request.form.get("password"):
                if (user.type == 1):
                    return redirect("/admin")
                elif (user.type == 2):
                    return redirect("/encargado")
                elif (user.type == 3):
                    return redirect("/colaborador")
                else:
                    return redirect("/cliente")
                
    return render_template("login.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/encargado")
def encargado():
    return render_template("encargado.html")

@app.route("/colaborador")
def colaborador():
    return render_template("colaborador.html")

@app.route("/cliente")
def cliente():
    return render_template("cliente.html")

if (__name__ == "__main__"):
    app.run(debug=True)



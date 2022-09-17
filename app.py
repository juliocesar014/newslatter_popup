from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

# colocar senha do email, senha para outros app

app = Flask(__name__)
app.secret_key = "julio"

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "jcprojetosx2@gmail.com"
app.config["MAIL_PASSWORD"] = "senha"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
mail = Mail(app)


class Contato:
    def __init__(self, email):
        self.email = email


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        formContato = Contato(request.form["email"])

        msg = Message(
            "Cadastro na Newslatter",
            sender="noreply@reply.com",
            recipients=["jcprojetosx2@gmail.com"],
        )

        msg.body = f"""
                Olá, quero ser cadastrado(a) na Newslatter,
                 meu e-mail é: {formContato.email}
            """

        mail.send(msg)
    return redirect("/sucess")


@app.route("/sucess")
def sucess():
    return render_template("sucess.html")


if __name__ == "__main__":
    app.run(debug=True)

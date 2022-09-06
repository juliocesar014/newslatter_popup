from flask import Flask, render_template, request
from flask_mail import Mail, Message
from config import email, senha

app = Flask(__name__)
app.secret_key = "python2022"

mail_settings = {
    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha,
}

app.config.update(mail_settings)

mail = Mail(app)


class EnviarEmail:
    def __init__(self, email):
        self.email = email


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        formEnviarEmail = EnviarEmail(request.form["email"])

        msg = Message(
            subject="Cadastro da newslatter",
            sender=app.config.get("MAIL_USERNAME"),
            recipients=[app.config.get("MAIL_USERNAME")],
            body=f"""

            Olá,
            Me cadaste na newslatter! Meu e-mail é: {formEnviarEmail.email}

            """,
        )
        mail.send(msg)


if __name__ == "__main__":
    app.run(debug=True)

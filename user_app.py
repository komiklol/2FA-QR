import pyotp
from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
from qrClass import qrCode

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'secretTest'

users = {
    "testuser": bcrypt.generate_password_hash("qwert123").decode("utf-8")
}

@app.route("/")
def index():
    return redirect("/v1/login")

@app.route("/v1/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users:
            if bcrypt.check_password_hash(users.get(username), password):
                # secret = pyotp.random_base32()
                secret = "N4E6BAYA4GAQ5S3WSLAN73LCXNOTPRXQ"

                session["user"] = username
                session["2fa_secret"] = secret

                user = session["user"]
                label = "TestApp"
                uri = f"otpauth://totp/{label}?secret={secret}&issuer={user}&algorithm=SHA1&digits=6&period=30"
                img = qrCode(uri).generate_qr()

                return render_template("login2FA.html", qr_code_image=img)
            else:
                return "Wrong password!"
        else:
            return "User not found!"

    return render_template("login.html")

@app.route("/v1/verify", methods=["POST"])
def verify():
    if "user" not in session:
        return redirect("/v1/login")

    user = session["user"]
    # secret = session["2fa_secret"]
    secret = "N4E6BAYA4GAQ5S3WSLAN73LCXNOTPRXQ"
    totp = pyotp.TOTP(secret)

    if totp.verify(request.form.get("2fa_code")):
        return redirect("/v1/totp/generate")
    else:
        return "Wrong code!"

@app.route("/v1/logout")
def logout():
    session.pop("user", None)
    return redirect("/v1/login")

@app.route("/v1/totp/generate" , methods=["GET", "POST"])
def generate_totp():
    qr_code_img = None

    # If method is POST, generate the QR code based on the form data
    if request.method == 'POST':
        data = request.form.get('text_data')
        if data:
            qr_code_img = qrCode(data).generate_qr()

    return render_template("template.html", qr_code_image=qr_code_img)

# TODO Add 2FA to the Login / New Website for 2FA
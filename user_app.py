import pyotp
from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
from qrClass import qrCode

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'secretTest'  # Secret key for Flask session

# Dictionary to store user credentials as username: hashed_password
users = {
    "testuser": bcrypt.generate_password_hash("qwert123").decode("utf-8")
}


@app.route("/")
def index():
    # Redirect to the login page
    return redirect("/v1/login")


@app.route("/v1/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get username and password from the login form
        username = request.form.get("username")
        password = request.form.get("password")

        # Verify if the username exists in the users dictionary
        if username in users:
            # Check if the provided password matches the hashed password
            if bcrypt.check_password_hash(users.get(username), password):
                # Hardcoded secret for TOTP
                # secret = pyotp.random_base32()
                secret = "N4E6BAYA4GAQ5S3WSLAN73LCXNOTPRXQ"

                # Store the logged-in user and secret in the session
                session["user"] = username
                session["2fa_secret"] = secret

                # Generate the OTP URI for the user
                user = session["user"]
                label = "TestApp"  # Label for the OTP application
                uri = f"otpauth://totp/{label}?secret={secret}&issuer={user}&algorithm=SHA1&digits=6&period=30"

                # Generate the QR code image for the OTP URI
                img = qrCode(uri).generate_qr()

                # Render the login2FA page with the QR code
                return render_template("login2FA.html", qr_code_image=img)
            else:
                # Return an error message for incorrect password
                return "Wrong password!"
        else:
            # Return an error message if the user is not found
            return "User not found!"

    # Render the login page for GET requests
    return render_template("login.html")


@app.route("/v1/verify", methods=["POST"])
def verify():
    # Redirect to login if user is not in the session
    if "user" not in session:
        return redirect("/v1/login")

    # Get the logged-in user and 2FA secret from the session
    user = session["user"]
    # secret = session["2fa_secret"]
    secret = "N4E6BAYA4GAQ5S3WSLAN73LCXNOTPRXQ"  # Hardcoded secret

    # Create a TOTP object using the secret
    totp = pyotp.TOTP(secret)

    # Verify the submitted 2FA code
    if totp.verify(request.form.get("2fa_code")):
        # Redirect to the TOTP generate page on successful verification
        return redirect("/v1/totp/generate")
    else:
        # Return an error message for incorrect 2FA code
        return "Wrong code!"


@app.route("/v1/logout")
def logout():
    # Remove the user from the session to log out
    session.pop("user", None)
    return redirect("/v1/login")


@app.route("/v1/totp/generate", methods=["GET", "POST"])
def generate_totp():
    qr_code_img = None

    # If method is POST, generate the QR code based on form data
    if request.method == 'POST':
        # Get the data for the QR code from the form
        data = request.form.get('text_data')
        if data:
            # Generate the QR code image using the qrCode class
            qr_code_img = qrCode(data).generate_qr()

    # Render the template with the QR code image
    return render_template("template.html", qr_code_image=qr_code_img)

# TODO Add 2FA to the Login / New Website for 2FA

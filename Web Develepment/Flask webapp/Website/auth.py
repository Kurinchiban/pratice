from flask import Blueprint

auth=Blueprint('auth',__name__)

@auth.route("/login")
def login():
    return "<h1>Login</h2>"

@auth.route("/logout")
def logout():
    return "<h1>Logout</h2>"

@auth.route("/sign-up")
def sign_up():
    return "<h1>Sign-up</h2>"
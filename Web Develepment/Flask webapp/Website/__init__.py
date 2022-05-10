from flask import Flask 

def create_app():
    app=Flask(__name__)
    app.config["SECREAT_KEY"]="jhndfujask uhasdgoiufg"
    
    from .view import views
    from .auth import auth

    
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")

    return app

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add")
def add_book():
    user=request.args.get('user')
    password=request.args.get('password')
    try:
        user=User(
            user=user,
            password=password
        )
        db.session.add(user)
        db.session.commit()
        return "User added. user id={}".format(user.id)
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        user=User.query.all()
        return  jsonify([e.serialize() for e in user])
    except Exception as e:
	    return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        user=User.query.filter_by(id=id_).first()
        return jsonify(user.serialize())
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    app.run()
from app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'user': self.user,
            'password': self.password,
        }
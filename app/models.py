from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    time = db.Column(db.DateTime, default=datetime.now)
    studentId = db.Column(db.String(20), primary_key=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    mobileNumber = db.Column(db.String(15), unique=True, nullable=False)
    pass_word = db.Column(db.String(60), nullable=False)

    def get_id(self):
        try:
            return self.studentId
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def __repr__(self):
        return 'User(%s , %s)' % (self.studentId, self.email)


class Candidate(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    contact = db.Column(db.String(15), unique=True, nullable=False)
    voteCount = db.Column(db.Integer, nullable=False)

    def get_id(self):
        try:
            return self.id
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    #def __repr__(self):
    #    return 'User(%s , %s)' % (self.studentId, self.email)

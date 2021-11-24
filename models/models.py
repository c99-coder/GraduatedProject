from app import db


class rabbitUser(db.Model):
    __tablename__ = 'rabbitUser'

    id = db.Column(db.String(20), primary_key=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    telephone = db.Column(db.String(11), nullable=False)
    rank = db.Column(db.Integer)


class otp(db.Model):
    __tablename__ = 'otp'

    id_index = db.Column(db.Integer, primary_key=True,
                         autoincrement=True)
    id = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    telephone = db.Column(db.String(11), nullable=False)
    rank = db.Column(db.Integer)
    settime = db.Column(db.DateTime),
    otpnum = db.Column(db.Integer, nullable=False)

from app import db

'''
model.py
이 파일은 데이터베이스의 제약 조건을 명시하는 파일입니다.
관계형 데이터베이스의 데이터를 객체랑 연결 시켜주는 것을 ORM (Object Relational Mapping) 이라고 불러요.
즉, 이 파일은 외부에 존재하는 DB를 서버에서 사용하기 위해, DB와 동일한 제약조건을 객체에 걸어버리는 겁니다.
'''


class rabbitUser(db.Model):

    # 테이블 이름입니다. 객체 이름과 달라도 되지만, 외부 테이블의 이름이 되기 때문에 유의해서 설정하세요.
    __tablename__ = 'rabbitUser'

    id = db.Column(db.String(20), primary_key=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(20))
    point = db.Column(db.Integer)
    address = db.Column(db.String(255))
    telephone = db.Column(db.String(11))
    rank = db.Column(db.Integer)

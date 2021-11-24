from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from models.models import *
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def home():
    user_list = rabbitUser.query.order_by(rabbitUser.nickname.asc())
    print(user_list)
    return render_template('main.html', user_list=user_list)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        # 회원가입 과정을 거쳐야겠다!
        # 만약에 같은 아이디가 있으면 어떡해?
        user = rabbitUser.query.filter_by(id=request.form['user_id']).first()

        if not user:
            password = generate_password_hash(request.form['password'])
            user = rabbitUser(id=request.form['user_id'], password=password,
                              nickname=request.form['nickname'], telephone=request.form['telephone'])

            db.session.add(user)
            db.session.commit()

            flash("회원가입이 완료되었습니다!")
            return redirect(url_for('main.home'))
        else:
            flash("이미 가입된 아이디입니다.")
            return redirect(url_for('main.register'))


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        id = request.form['user_id']
        password = request.form['password']

        user_data = rabbitUser.query.filter_by(id=id).first()

        if not user_data:
            flash("없는 아이디입니다.")
            return redirect(url_for('main.login'))
        elif not check_password_hash(user_data.password, password):
            flash("비밀번호가 틀렸습니다.")
            return redirect(url_for('main.login'))
        else:
            session.clear()
            session['user_id'] = id
            session['nickname'] = user_data.nickname

            flash("로그인 성공")
            return redirect(url_for('main.home'))


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.home'))

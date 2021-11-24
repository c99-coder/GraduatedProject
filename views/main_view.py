import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from base64 import b32encode
import pyotp
import datetime
from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from models.models import *
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def home():
    user_list = rabbitUser.query.order_by(rabbitUser.nickname.asc())
    return render_template('main.html', user_list=user_list)


@bp.route('/otpCheck', methods=('GET', 'POST'))
def otpCheck(id=None):
    if request.method == 'GET':
        id = request.args.get('id')
        return render_template('otpCheck.html', id=id)
    elif request.method == 'POST':
        id = request.args.get('id')
        otp_key = b32encode(id.encode())
        totp = pyotp.TOTP(otp_key, interval=300)
        otpnum = totp.now()

        if int(otpnum) == int(request.form['otpnum']):
            user_data = otp.query.filter(otp.id == id).first()
            print(user_data)
            user = rabbitUser(id=user_data.id, password=user_data.password,
                              nickname=user_data.nickname,
                              email=user_data.email,
                              telephone=user_data.telephone)

            db.session.add(user)
            db.session.commit()

            print(totp.now())
            flash("회원가입이 완료되었습니다!")
            return redirect(url_for('main.home'))
        else:
            flash("OTP를 다시 확인해주세요.")
            return redirect(url_for('main.otpCheck', id=id))


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        # 아이디 중복 체크
        user = rabbitUser.query.filter_by(id=request.form['user_id']).first()

        if not user:
            otp_key = b32encode(request.form['user_id'].encode())
            totp = pyotp.TOTP(otp_key, interval=300)
            otpnum = totp.now()
            print(totp.now())
            password = generate_password_hash(request.form['password'])
            user = otp(id=request.form['user_id'], password=password,
                       nickname=request.form['nickname'],
                       email=request.form['email'],
                       telephone=request.form['telephone'],
                       settime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                       otpnum=otpnum)

            db.session.add(user)
            db.session.commit()

            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login('knpcjg3@gmail.com', 'rzamllpqmtfgxlwq')

            msg = MIMEText(f'OTP Number is:{otpnum}')
            msg['Subject'] = '졸업과제OTP'

            s.sendmail("knpcjg3@gmail.com",
                       request.form['email'], msg.as_string())
            s.quit()

            return redirect(url_for('main.otpCheck', id=request.form['user_id']))
        else:
            flash("이미 가입된 아이디입니다.")
            return redirect(url_for('main.register'))


@ bp.route('/login', methods=('GET', 'POST'))
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


@ bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.home'))

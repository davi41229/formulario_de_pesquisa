from flask import render_template, url_for, request, redirect
from app import app, db
from flask_login import login_user, logout_user
from app.models.models import Pesquisa

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']

        pesquisa = Pesquisa(name,email,pwd)
        db.session.add(pesquisa)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        pesquisa = Pesquisa.query.filter_by(email=email).first()
        
        if not pesquisa or not pesquisa.verify_password(pwd):
            return redirect(url_for('login'))

        login_user(pesquisa)
        return redirect(url_for('form'))

    return render_template('login.html')


@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        return redirect(url_for('Index'))
    return render_template('form.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True,port=(4000))

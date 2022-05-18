from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import RegForm, LoginForm, CandForm, UpdateUserForm
from app.models import User, Candidate
from app import app, db, pwd
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def homepage():
    return render_template("information.html", )


@app.route("/signup", methods=['GET', 'POST'])
def signuppage():
    if current_user.is_authenticated:
        flash("You are already logged in.", "warning")
        return redirect(url_for("homepage"))
    form = RegForm(request.form)
    if request.method == "POST" and form.validate():
        hashed = pwd.generate_password_hash(form.pass_word.data).decode('utf-8')
        element = User(studentId=form.studentId.data, name=form.name.data, email=form.email.data,
                       mobileNumber=form.mobileNumber.data, pass_word=hashed)
        db.session.add(element)
        db.session.commit()
        flash("Account created for %s!" % (form.studentId.data), "success")
        return redirect(url_for("loginpage"))
    return render_template("signup.html", form=form)


@app.route("/cand_signup", methods=['GET', 'POST'])
def cand_signuppage():
    if current_user.is_authenticated:
        flash("You are already logged in.", "warning")
        return redirect(url_for("homepage"))
    form = CandForm(request.form)
    if request.method == "POST" and form.validate():
        element = Candidate(name=form.name.data, email=form.email.data, contact=form.contact.data)
        db.session.add(element)
        db.session.commit()
        flash("New Nomination Registered %s!" % (form.name.data), "success")
        # return redirect(url_for("loginpage"))
    return render_template("cand_signup.html", form=form)


@app.route("/login", methods=['GET', 'POST'])
def loginpage():
    if current_user.is_authenticated:
        flash("You are already logged in.", "warning")
        return redirect(url_for("homepage"))
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        member = User.query.filter_by(studentId=form.studentId.data).first()
        if member and pwd.check_password_hash(member.pass_word, form.pass_word.data):
            login_user(member)
            flash("Welcome, %s!" % (form.studentId.data), "success")
            return redirect(url_for("homepage"))
        else:
            flash("Username or Password doesn't match, please try again.", "danger")
            return redirect(url_for("loginpage"))
    return render_template("login.html", form=form)


@app.route("/logout")
def logoutpage():
    logout_user()
    flash("Successfuly logged out.", "success")
    return redirect(url_for("homepage"))


@app.route("/member-page")
@login_required
def member():
    return render_template("members.html")


@app.route("/edit-member", methods=['GET', 'POST'])
@login_required
def edit_member():
    if current_user.is_authenticated:
        user = User.query.filter_by(studentId=current_user.studentId).first()
        form = UpdateUserForm(request.form)
        if request.method == "POST" and form.validate():
            element = User(studentId=current_user.studentId, name=form.name.data, email=form.email.data,
                           mobileNumber=form.mobileNumber.data, pass_word=current_user.pass_word)
            db.session.add(element)
            db.session.commit()
            flash("Account created for %s!" % (form.studentId.data), "success")
            return redirect(url_for("edit_member"))
        return render_template("edit_member.html", form=form)

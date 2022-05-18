from wtforms import Form, StringField, PasswordField, SubmitField, validators
from app.models import User, Candidate


class RegForm(Form):
    studentId = StringField("Username", validators=[
        validators.DataRequired(),
        validators.Length(min=4, message="Username must be at least 6 characters long.")
    ])
    name = StringField("Name", validators=[
        validators.DataRequired(),
        validators.Length(min=2, message="Name must be at least 2 characters long.")
    ])
    email = StringField("E-Mail", validators=[
        validators.DataRequired(),
        validators.Email(),
        validators.Length(min=6, message="Email Address must be at least 6 characters long.")
    ])
    mobileNumber = StringField("Mobile", validators=[
        validators.DataRequired(),
        validators.Length(min=10, message="Number must be at least 10 digits long.")
    ])
    pass_word = PasswordField("Password", validators=[
        validators.DataRequired(),
        validators.Length(min=4, message="Password must be at least 4 characters long.")
    ])
    confirm = PasswordField("Confirm Password", validators=[
        validators.EqualTo('pass_word', message="Passwords do not match."),
        validators.DataRequired()
    ])
    submit = SubmitField("Sign Up")

    def validate_studentId(self, studentId):
        present = User.query.filter_by(studentId=studentId.data).first()
        if present:
            raise validators.ValidationError("This username has already been taken, please choose a different one.")

    def validate_email(self, email):
        present = User.query.filter_by(email=email.data).first()
        if present:
            raise validators.ValidationError(
                "This email has already been registered with us, please enter a different one.")


class LoginForm(Form):
    studentId = StringField("Username", validators=[
        validators.DataRequired(),
        validators.Length(min=4, max=20)
    ])
    pass_word = PasswordField("Password", validators=[
        validators.DataRequired(),
        validators.Length(min=4, max=20)
    ])
    submit = SubmitField("Login")


class CandForm(Form):
    name = StringField("Name", validators=[
        validators.DataRequired(),
        validators.Length(min=2, message="Name must be at least 2 characters long.")
    ])
    email = StringField("E-Mail", validators=[
        validators.DataRequired(),
        validators.Email(),
        validators.Length(min=6, message="Email Address must be at least 6 characters long.")
    ])
    contact = StringField("Mobile", validators=[
        validators.DataRequired(),
        validators.Length(min=10, message="Number must be at least 10 digits long.")
    ])
    submit = SubmitField("Register")


class UpdateUserForm(Form):
    studentId = StringField("Username", validators=[
        validators.DataRequired(),
        validators.Length(min=4, message="Username must be at least 6 characters long.")
    ])
    name = StringField("Name", validators=[
        validators.DataRequired(),
        validators.Length(min=2, message="Name must be at least 2 characters long.")
    ])
    email = StringField("E-Mail", validators=[
        validators.DataRequired(),
        validators.Email(),
        validators.Length(min=6, message="Email Address must be at least 6 characters long.")
    ])
    mobileNumber = StringField("Mobile", validators=[
        validators.DataRequired(),
        validators.Length(min=10, message="Number must be at least 10 digits long.")
    ])
    pass_word = PasswordField("Password", validators=[
        validators.DataRequired(),
        validators.Length(min=4, message="Password must be at least 4 characters long.")
    ])
    submit = SubmitField('Update')

    #def validate_email(self, email):
    #    if User.query.filter_by(email=email.data).first():
    #        raise validators.ValidationError('This email has been registered already!')

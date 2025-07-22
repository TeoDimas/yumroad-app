from flask_wtf import FlaskForm

from wtforms.fields import StringField, SubmitField
from wtforms.validators import Length

class ProductForm(FlaskForm):
    name = StringField('Name', [Length(min=4, max=60)])
    description = StringField('Description')
    submit = SubmitField('Create')class LoginForm(FlaskForm):
    email = StringField('Email', validators=[validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])

    def validate(self, extra_validators=None):
        check_validate = super(LoginForm, self).validate()
        if not check_validate:
            return False

        user = User.query.filter_by(email=self.email.data).first()
        if not user:
            self.email.errors.append('Invalid email or password')
            return False

        if not check_password_hash(user.password, self.password.data):
            self.email.errors.append('Invalid email or password')
            return False
        return True

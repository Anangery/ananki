import flask
import wtforms
import flask_wtf

class CardForm(flask_wtf.FlaskForm):
    front = wtforms.StringField("Front", validators=[wtforms.validators.DataRequired()])
    back = wtforms.StringField("Back", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Submit")

class EditForm(flask_wtf.FlaskForm):
    front = wtforms.StringField("Front", validators=[wtforms.validators.DataRequired()])
    back = wtforms.StringField("Back", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Submit")

class NameForm(flask_wtf.FlaskForm):
    name = wtforms.StringField("name", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Submit name")
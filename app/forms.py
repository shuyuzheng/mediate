from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateField, SelectField
from wtforms.validators import Optional

class SearchForm(FlaskForm):
    query = StringField('Key word')
    critics_pick = BooleanField("Only critics' pick")
    opening_start = DateField(format="%Y-%m-%d", validators=[Optional()])
    opening_end = DateField(format="%Y-%m-%d", validators=[Optional()])
    publication_start = DateField(format="%Y-%m-%d", validators=[Optional()])
    publication_end = DateField(format="%Y-%m-%d", validators=[Optional()])
    reviewer = StringField('Reviewer')
    order = SelectField('Order results by', choices=[('by-opening-date', 'Opening date'), ('by-publication-date', 'Publication date'), ('by-title', 'Title')])
    submit = SubmitField('Search')

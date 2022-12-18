from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired
from src.main import game


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'


class LotteryForm(FlaskForm):
    format = IntegerField('Format', validators=[DataRequired()])
    from_num = IntegerField('From', validators=[DataRequired()])
    tickets = IntegerField('Tickets', validators=[DataRequired()])
    submit = SubmitField('Generate')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = LotteryForm()
    tickets = []
    draw = []
    if form.validate_on_submit():
        draw, tickets = game(form.format.data, form.from_num.data, form.tickets.data)
    return render_template('index.html', form=form, draw=draw, tickets=tickets)


if __name__ == '__main__':
    app.run(debug=True)

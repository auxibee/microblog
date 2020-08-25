from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators  import DataRequired
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'auxibee'

class AgreementForm(FlaskForm):

    applicant = StringField('Applicant:',validators=[DataRequired()])
    guarantor_one = StringField('Guarantor one:',validators=[DataRequired()])
    guarantor_two = StringField('Guarantor Two:',validators=[DataRequired()])
    amount = StringField('Amount:',validators=[DataRequired()])
    submit            = SubmitField('Add')



@app.route('/',methods=['GET','POST'])
def hello():
    form = AgreementForm()
    date = datetime.date.today()
    if form.validate_on_submit():
        applicant = form.applicant.data
        guarantor_one = form.guarantor_one.data
        guarantor_two = form.guarantor_two.data
        amount = form.amount.data
        return render_template('contract.htm',applicant=applicant,guarantor_one=guarantor_one,guarantor_two=guarantor_two,amount=amount,date=date)
    return render_template('index.htm',form=form)

if __name__ == '__main__':
    app.run(debug=True)
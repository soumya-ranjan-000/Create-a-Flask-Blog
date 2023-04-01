from flask import Flask,render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app=Flask(__name__)

app.config['SECRET_KEY']="PYTHON is love"

#Create a Form Class
class NameForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    name.flags="false"
    submit=SubmitField("Submit")



@app.get('/home')
@app.get('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    return render_template('register.html')

@app.route('/user/<name>',methods=['GET','POST'])
def user_profile(name):
    return render_template('UserProfile.html',name=name)

@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_404(e):
    return render_template('500.html'), 500

# Create a Name pAge
@app.route('/name',methods=['GET','POST'])
def name():
    name=None
    form=NameForm()
    #Validate Form
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
        flash("Form Submitted Successfully!")
    return render_template('name.html',name=name,form=form)


if __name__ == "__main__":
    app.run(port=8080,debug=True)


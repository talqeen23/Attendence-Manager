from pitho import app
from flask import render_template,request,session,redirect
from pitho.models.user.model_register import RegisterModel
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SelectField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email
class RegisertMyForm(FlaskForm):
	fname=StringField("First Name",validators=[DataRequired()])
	lname=StringField("Last Name",validators=[DataRequired()])
	email=StringField("Email",validators=[DataRequired(),Email()])
	password=PasswordField("Password",validators=[DataRequired(),Length(min=8)])
	user_type=SelectField("User Type",choices=[('1',"Student"),('2',"Teacher")])
	checkbox=BooleanField("Terms and Condition")
@app.route("/register",methods=['GET','POST'])
def user_register():
	data=request.form;
	wform=RegisertMyForm(request.form)
	obj=RegisterModel()
	if wform.validate_on_submit():
		status=obj.register(data)
		if status==True:
			return redirect("/")
	return render_template("user/register.html",form=wform);
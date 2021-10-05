from pitho import app
from flask import render_template,request,session,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Length,Email
from pitho.models.user.model_forgotpassword import ForgotPassword
class MyForm(FlaskForm):
	youremail=StringField("Email",validators=[DataRequired(),Email()])
	otp=StringField("OTP")
	resetpassword=PasswordField("ResetPassword")
@app.route("/forgotpassword",methods=['GET','POST'])
def user_forgotpassword():
	message=""
	otpstatus=False
	passstatus=False
	wform=MyForm(request.form)
	if wform.validate_on_submit():
		obj=ForgotPassword()
		status=obj.forgot_password(request.form)
		if status==True:
			return redirect("/")
	if session.get('otpshow') is not None:
		otpstatus=True
	if session.get('showpass') is not None:
		passstatus=True
	return render_template("user/forgotpassword.html",form=wform,otp=otpstatus,passw=passstatus);
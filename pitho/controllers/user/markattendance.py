from pitho import app
from flask import render_template,request,session,redirect
from pitho.models.user.model_markattendance import ModelMarkAttendance
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class MyForm(FlaskForm):
	markin=StringField("Mark In",validators=[DataRequired()],default=1)
@app.route("/mark-attendance",methods=['GET','POST'])
def mark_attendance():
	if session.get("logged_in") is None:
		return redirect("/")
	form=MyForm(request.form)
	obj=ModelMarkAttendance()
	if form.validate_on_submit():
		status=obj.mark_attendance(request.form)
		if status==True:
			return redirect("/mark-attendance")
	mark_in_check=obj.check_today_present()
	mark_out_check=obj.check_today_out()
	return render_template("user/markattendance.html",form=form,mark_in_check=mark_in_check,mark_out_check=mark_out_check)
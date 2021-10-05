from pitho import app
from flask import render_template,request,session,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired,Email,NumberRange
from pitho.models.user.model_editprofile import EditProfile
from pitho.models.user.model_dashboard import UserDashboard
class MyForm(FlaskForm):
	name=StringField("Name",validators=[DataRequired()])
	email=StringField("Email",validators=[DataRequired(),Email()])
	number=IntegerField("Phone Number",validators=[NumberRange()])
@app.route("/editprofile",methods=['GET','POST'])
def user_editprofile():
	message=""
	uobj=UserDashboard()
	teachers=uobj.get_teacher()
	obj=EditProfile()
	row=obj.getprofile_data()
	wform=MyForm(request.form,name=row['name'],email=row['email'],number=row['phone'])
	if wform.validate_on_submit():
		status=obj.update_profile(request.form)
		if status==True:
			return redirect("/dashboard")
	return render_template("user/editprofile.html",data=message,form=wform,users_list=teachers,row=row)
	
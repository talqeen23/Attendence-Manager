from pitho import app
from flask import render_template,session,request,redirect
from pitho.models.author.model_viewprofile import ModelViewProfile
@app.route("/view-profile/<id>",methods=['GET','POST'])
def view_profile(id=0):
	obj=ModelViewProfile()
	student=obj.get_student(id)
	student=obj.check_markin()
	student=obj.check_markout()
	student=obj.mark_attendance(request.form)
	return render_template("author/viewprofile.html",student=student)
	
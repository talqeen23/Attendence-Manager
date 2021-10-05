from pitho import app
from flask import render_template,session
from pitho.models.author.model_authordashboard import ModelAuthorDashboard
@app.route("/author-dashboard",methods=['GET','POST'])
def author_dashboard():
	if session.get("logged_in") is None:
		return redirect("/")
	obj=ModelAuthorDashboard()
	data=obj.get_student()
	return render_template("author/dashboard.html",student_list=data)
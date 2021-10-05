from pitho import app
from flask import render_template,session
from pitho.models.author.model_todayattendance import ModelTodayAttendance
@app.route("/author-todayattendance")
def author_todayattendance():
	if session.get("logged_in") is None:
		return redirect("/")
	obj=ModelTodayAttendance()
	data=obj.today_attendance() 
	return render_template("author/todayattendance.html",todayattendance=data);
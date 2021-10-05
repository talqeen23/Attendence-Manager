from pitho import app
from flask import render_template,request,session,redirect
@app.route("/dashboard")
def dashboard():
	if session.get("logged_in") is None:
		return redirect("/")
	if session.get("user_type")==2:
		return redirect("/author-dashboard")
	id=session.get("logged_in")
	return render_template("user/dashboard.html");

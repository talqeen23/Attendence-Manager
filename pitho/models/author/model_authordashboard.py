from flask import Flask,flash,session
from pitho.Config import conn
class ModelAuthorDashboard():
	def get_student(self):
		user_id=session.get("logged_in")
		db=conn.connection.cursor()
		db.execute("select * from users where class_teacher=%s",(str(user_id)))
		data=db.fetchall()
		return data
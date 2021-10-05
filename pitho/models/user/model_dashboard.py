from flask import Flask,flash,session
from pitho.Config import conn
class UserDashboard():
	def get_teacher(self,type=2):
		db=conn.connection.cursor()
		db.execute("select id,name from users where user_type=%s",(str(type)))
		data=db.fetchall();
		return data
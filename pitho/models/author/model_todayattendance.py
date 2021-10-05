from flask import Flask,flash,session
from pitho.Config import conn
import datetime
class ModelTodayAttendance():
	def today_attendance(self):
		teacher_id=session.get("logged_in")
		date=datetime.datetime.now()
		today=date.strftime("%Y-%m-%d")
		db=conn.connection.cursor()
		db.execute("select u.name,m.mark_in,m.mark_out  from users as u join mark_attendance as m on m.user_id=u.id where m.date_time=%s",(today))
		data=db.fetchall()
		return data
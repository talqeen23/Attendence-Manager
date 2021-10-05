from flask import Flask,flash,session
from pitho.Config import conn
import datetime
class ModelViewProfile():
	def get_student(self,id):
		db=conn.connection.cursor()
		db.execute("select u.name,u.email,m.* from users as u join mark_attendance as m on m.user_id=u.id where u.id=%s",(str(id)))
		row=db.fetchall()
		return row
	def mark_attendance(self,data):
		user_id=session.get("logged_in")
		mark_att=data.get("markin")
		mark=data.get("mark")
		db=conn.connection.cursor()
		db.execute("select class_teacher from users where id=%s",(str(user_id)))
		row=db.fetchone()
		class_teacher=row['class_teacher']
		db=conn.connection.cursor()
		dates=datetime.datetime.now()
		current_date=dates.strftime("%Y-%m")
		if mark=="Mark In":
			db.execute("insert into mark_attendance(user_id,mark_in,class_teacher,date_time)values(%s,%s,%s,%s)",(str(user_id),str(mark_att),str(class_teacher),current_date))
		else:
			db.execute("insert into mark_attendance(user_id,mark_out,class_teacher,date_time)values(%s,%s,%s,%s)",(str(user_id),str(mark_att),str(class_teacher),current_date))
		conn.connection.commit()
		flash(mark)
		return True
	def check_markin(self):
		user_id=session.get("logged_in")
		db=conn.connection.cursor()
		dates=datetime.datetime.now()
		current_date=dates.strftime("%Y-%m")
		db.execute("select id from mark_attendance where user_id=%s and mark_in=%s and date_time=%s",(str(user_id),str('1'),current_date))
		data=db.fetchone()
		if data is not None:
			return True
		else:
			return False
	def check_markout(self):
		user_id=session.get("logged_in")
		db=conn.connection.cursor()
		dates=datetime.datetime.now()
		current_date=dates.strftime("%Y-%m")
		db.execute("select id from mark_attendance where user_id=%s and mark_out=%s and date_time=%s",(str(user_id),str('1'),current_date))
		data=db.fetchone()
		if data is not None:
			return True
		else:
			return False
		
from pitho import app
from flask_mail import Mail,Message
mail=Mail(app)
app.config['MAIL_SERVER']="smtp.gmail.com"
app.config['MAIL_PORT']="587"
app.config['MAIL_USERNAME']="akashrajpoot2218@gmail.com"
app.config['MAIL_PASSWORD']="9720636184"
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False
def mailer(subject,message,reciever):
	msg=Message(subject,sender="akashrajpoot2218@gmail.com",recipients=[reciever])
	msg.body=message
	mail.send(msg)
	return True;
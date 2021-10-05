import subprocess

def install(name):
    subprocess.call(['pip', 'install', name])
install("flask");
install("pymysql")
install("flask_mail")


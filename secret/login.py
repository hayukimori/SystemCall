from PyQt5 import uic, QtWidgets
from pygame import mixer as mx
import os


os.system("echo $HOME > home")
arquivo = open("home", 'r')
tmp = arquivo.read()
home = tmp.replace('\n', '')

homezero = home+"/SystemCallApp/secret/"


def logged_screen():
	login.label_4.setText("")
	username = login.username.text()
	password = login.password.text()

	if username == "hayukimori" and password == "saolinkstart":
		print (username + '/' + password)



		login.close()
		mx.init()
		mx.music.load(homezero+"sao_2_dead.mp3")
		mx.music.play()
		logged.show()
	if username == "sudouser" and password == "sudo":

		login.close()
		admin.show()
	else:
		login.label_4.setText("username or password incorrect")
def logout():
	logged.close()
	login.show()

def shell():
	import os
	command = admin.commandline.text()
	if (command == "quit"):
		admin.close()
		login.show()
	else:
		os.system("ls /bin")
		print("----------------------------------")
		admin.result.setText(command)
		os.system(command + " > temp.txt")
		temp = open("temp.txt","r")
		show = temp.read()

		shell = admin.result.setText(command + '\n' + show)
		temp.close()
		os.system("rm temp.txt")



app = QtWidgets.QApplication([])
login = uic.loadUi(home+"/SystemCallApp/secret/login.ui")
logged = uic.loadUi(home+"/SystemCallApp/secret/logged.ui")
admin = uic.loadUi(home+"/SystemCallApp/secret/sudouser.ui")
login.login_button.clicked.connect(logged_screen)
logged.logout.clicked.connect(logout)
admin.sh.clicked.connect(shell)
login.password.setEchoMode(QtWidgets.QLineEdit.Password)

arquivo.close()

mx.init()
mx.music.load(homezero+"sao_menu.mp3")
mx.music.play()
login.show()


app.exec()


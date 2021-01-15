import time, os
from PyQt5 import uic, QtWidgets
from pygame import mixer as mx


os.system("echo $HOME > home")

arquivo = open("home", 'r')
tmp = arquivo.read()
home = tmp.replace('\n', '')


def stacia_command():
    os.system("echo $USER > tmp")
    tmp = open('tmp', 'r')
    uid = tmp.readline(10)
    
    stacia.id.setText('['+uid+']')
    
    tmp.close()
    os.system('rm tmp')
    mx.init()
    mx.music.load(home+"/SystemCallApp/assets/se/StaciaSound_1.mp3")
    mx.music.play()
    stacia.show()
    
    

app = QtWidgets.QApplication([])
stacia = uic.loadUi(home+"/SystemCallApp/staciawindow.ui")
arquivo.close()
os.system("rm home")
stacia_command()
app.exec()


#Make desktop entry
import os

os.system("echo $HOME > userhome")
tmp = open("userhome",'r')
user = tmp.read()
home = user.replace('\n','')



arquivo = "[Desktop Entry]\nVersion=1.0\nName=System Call\nExec=xterm -e python3 "" + home + ".local/share/SystemCallApp/main.py" \nTerminal=false\nType=Application\nStartupNotify=true"

os.system('echo "' + arquivo + '" > systemcall-py.desktop')

tmp.close()
os.system("rm userhome")

print("feito")

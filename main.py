import time, os
from pygame import mixer as mx
import speech_recognition as sr

#coding: utf-8


os.system("echo $HOME > home")
arquivo = open("home", 'r')
tmp = arquivo.read()
home = tmp.replace('\n', '')

def start():
    #ativar microfone
    microphone = sr.Recognizer()

    #inicia o microfone
    with sr.Microphone() as source:

        #reduzir ruidos
        microphone.adjust_for_ambient_noise(source)


        #receber chamada do sistema
        audio = microphone.listen(source)

    try:

        #passa a variavel para o algoritmo do google
        syscall = microphone.recognize_google(audio,language='en')

        #retornar
        print('Master: ' + syscall)

    #se nao reconheceu o padrao de fala
    except sr.UnknownValueError:
        print("ERROR")
        start()

    if (syscall.lower() == "system call" or syscall.lower() == "systemcall" or syscall.lower() == "system"):
        main()
    elif (syscall.lower() == "link start" or syscall.lower() == "linkstart"):
        os.system("python3 secret/login.py")
    else:
        start()
    

def main():
    microphone = sr.Recognizer()
    with sr.Microphone() as source:

        microphone.adjust_for_ambient_noise(source)

        print("command:")


        recebimento = microphone.listen(source)

    try:

        #google dnv
        command = microphone.recognize_google(recebimento,language='ja')

        #retorna o comando
        print(command)
        
        
        
        #generate umbra element
        if (command == "ジェネレート umbra エレメント" or command == "ジェネレート アンブラ エレメント" or command == "ジェネレートアンブラエレメント"):
            os.system("sudo gnome-terminal")
            main()

	#genrate luminous element
        if (command == "ジェネレートルミナスエレメント" or command == "ジェネレート ルミナス エレメント"):
            os.system("gnome-terminal")
            main()

        if(command == "オープン ノート" or command == "オープンノート"):
            os.system("xterm nano")
            main()
            
        
        
        #inspect list
        """
        if (command == "インスペクトリスト" or command == "インスペクト リスト" or command == "Inspect List"):
            
            os.system("python3 $HOME/SystemCallApp/commandlist.py &")
            
	    main()
        """
        
        
        #JANELA STACIA
        if (command.lower() == "info" or command.lower() == "stacia" or command.lower() == "window"):
            os.system("python3 $HOME/SystemCallApp/stacia.py &")
            
            main()
            
            
        #Logout
        if (command.lower() == "exit" or command.lower() == "quit" or command.lower() == "cancel" or command.lower() == "logout"):
            quit()
            
            
        else:
            mx.init()
            mx.music.load(home+"/SystemCallApp/assets/se/error.mp3")
            mx.music.play()
            main()
    #se n reconheceu o comando:
    except sr.UnknownValueError:
        print(".")
        main()

"""
def stacia_command():
    os.system("echo $USER > tmp")
    tmp = open('tmp', 'r')
    uid = tmp.readline(10)
    
    stacia.id.setText('['+uid+']')
    
    tmp.close()
    os.system('rm tmp')
    stacia.show()
"""



start()


arquivo.close()

import time
import os
from pygame import mixer
import speech_recognition as sr


def init():
	#ativar microfone
	microphone = sr.Recognizer()

	#inicia o microfone
	with sr.Microphone() as source:

		#reduzir ruidos
		microphone.adjust_for_ambient_noise(source)

		os.system("clear")

		#receber chamada do sistema
		audio = microphone.listen(source)

	try:

		#passa a variavel para o algoritmo do google
		syscall = microphone.recognize_google(audio,language='ja')

		#retornar
		print('Master: ' + syscall)

	#se nao reconheceu o padrao de fala
	except sr.UnknownValueError:
		print("ERROR")
		init()

	if (syscall == "システムコール"):
		main()
	if (syscall == "システム コール"):
		main()
	if (syscall == "systemcall"):
		main()
	if (syscall == "hayukimori"):
		os.system("nano SystemCall.py")
	else:
		print(" ")
		init()



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


	#se n reconheceu o comando:
	except sr.UnknownValueError:
		print(".")
		main()


#inspect list
	if (command == "インスペクトリスト"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/sao.mp3')
		mixer.music.play()
		os.system("./.syscall/comandos.sh")
		main()

	if (command == "インスペクト リスト"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/sao.mp3')
		mixer.music.play()
		os.system("./.syscall/comandos.sh")
		main()

	if (command == "Inspect List"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/sao.mp3')
		mixer.music.play()
		os.system("./.syscall/comandos.sh")
		main()

	if (command == "インスペクト コマンド リスト"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/sao.mp3')
		mixer.music.play()
		os.system("ls /bin")
		time.sleep(20)
		main()
		
	if (command == "インスペクトコマンドリスト"):
		os.system("ls /bin")
		time.sleep(20)
		main()
	if (command == "インスペクト コマンドリスト"):
		os.system("ls /bin")
		time.sleep(20)
		main()

#inspect element
	if (command == "インスペクトエレメント"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/ow_dva_mech_sfx_5.mp3')
		mixer.music.play()
		os.system("gnome-terminal --working-directory=/usr/share")
		time.sleep(10)
		main()

#generate umbra element
	if (command == "ジェネレートアンブラエレメント"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/umbra.mp3')
		mixer.music.play()
		os.system("sudo gnome-terminal")
		main()

	if (command == "ジェネレート umbra エレメント"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/umbra.mp3')
		mixer.music.play()
		os.system("sudo gnome-terminal")
		main()

	if (command == "ジェネレート アンブラ エレメント"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/umbra.mp3')
		mixer.music.play()
		os.system("sudo gnome-terminal")
		main()

#genrate luminous element
	if (command == "ジェネレートルミナスエレメント"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/ow_dva_mech_sfx_4.mp3')
		mixer.music.play()
		os.system("gnome-terminal")
		main()

	if (command == "ジェネレート ルミナス エレメント"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/sao_2_dead.mp3')
		mixer.music.play()
		os.system("gnome-terminal")
		main()


	#remove core protection= n tenho ideia

	#form object - abrir um editor de foto/video ou texto

	#transfer human unit durability,self to left = reduzir ou aumentar brilho da tela
	if (command == "トランスファー デュラビリティ"):
		print("beta ver. not finalized")
		os.system("echo 'wait for update'")

	#generate blizzard gate - zero one deixa as letras do terminal branco
	if (command == "ジェネレート ブリザルド ゲート"):
		print("")
		main()

	if (command == "ジェネレート ブリザードゲート"):
		print("")
		main()


	#change field atribution = muda o usuario para padrão

	#redefinition object - rod class = reboota o pc
	if (command=="redefinition object"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/ow_dva_mech_sfx_3.mp3')
		mixer.music.play()
		print("rebooting system...")
		os.system("reboot")


	if (command=="definition OBJECT"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/ow_dva_mech_sfx_3.mp3')
		mixer.music.play()
		print("rebooting system...")
		os.system("reboot")
	#lightning deixa o brilho no maximo






#ENHANCE ARMAMENT
	if (command == "エンハンス アーマメント"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/')
		mixer.music.play()
		os.system("gpicview $HOME/Imagens")
		init()
		
#jikan
	if (command == "時間"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/bob_notification.mp3')
		mixer.music.play()
		os.system("date")
		time.sleep(5)
		main()

	if (command == "今は何時ですか"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/bob_notification.mp3')
		mixer.music.play()
		os.system("date")
		time.sleep(5)
		main()

	if (command == "今は"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/bob_notification.mp3')
		mixer.music.play()
		os.system("date")
		time.sleep(5)
		main()

#LINK START

	if (command == "リンクスタート"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/link_start.mp3')
		mixer.music.play()
		os.system('firefox https://sao-p.net')
		main()
#STACIA
	if (command == "スタシア"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/dangaronpa_pc_sfx.mp3')
		mixer.music.play()
		os.system("python3 stacia.py")
		main()

	if (command == "STACIA"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/dangaronpa_pc_sfx.mp3')
		mixer.music.play()
		os.system("python3 stacia.py")
		main()

#open note

	if(command == "オープン ノート"):
		os.system("leafpad")
		main()
	if(command == "オープンノート"):
		os.system("leafpad")
		main()

#cancel (kyanseru)
	if (command == "キャンセル"):
		mixer.init()
		mixer.music.load('.syscall/sound_effects/sao_2_dead.mp3')
		mixer.music.play()
		exit()
#else
	else:
		print(" ")
		main()


	

init()

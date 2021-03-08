#!/bin/bash

clear
echo "Cardinal - Para instalar o SystemCall.py, preciso da sua permissão!"
echo
echo "Os pacotes a serem instalados são: python3, python3-pip, SpeechRecognition, pyqt5 e pygame"
echo "Você pode verificar isto abrindo este script de instalação"
Continuar(){
    echo
    echo
    echo "Instalação do SystemCall.py"
    echo
    echo -n ":: Continuar a instalação? [S/n] "
    read aceitar
  case $aceitar in
        s) dependencias;;
        n)echo "Instalação cancelada pelo usuário!" && exit;;
        *) dependencias
  esac
}

dependencias(){
 which apt >/dev/null 2>&1
if [ $? -eq 0 ]
then
    sudo apt-get install xterm git python3 python3-pip -y
fi
which pacman >/dev/null 2>&1
if [ $? -eq 0 ]
then
    sudo pacman -S xterm git python3 python-pip xterm --noconfirm
fi

# Dependencias do python
clear
echo "Iniciando a instalação dos pacotes Python"
echo
pip3 install SpeechRecognition
pip3 install pyqt5
pip3 install pygame
pip3 install pyaudio

# Download & Install SystemCall
clear
echo
echo "Baixando arquivos..."
echo
git clone https://github.com/RedsonBr140/SystemCall.git
mkdir $HOME/.local/share/SystemCallApp
# install
cp -r SystemCall/* $HOME/.local/share/SystemCallApp

# Criando o Shortcut
echo "Criando atalho no menu"
cp SystemCall/systemcall-py.desktop $HOME/.local/share/applications/
}
Continuar

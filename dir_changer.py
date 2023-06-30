import os

venv_dir = "/home/diaoko/venv"
cur_dir = os.getcwd()

def show_dir():
    print("current dir is: ")
    print(os.getcwd())


if (cur_dir != venv_dir) :
    os.chdir(venv_dir)

show_dir()
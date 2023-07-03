import os

venv_dir = "/home/diaoko/venv"
cur_dir = os.getcwd()

if (cur_dir != venv_dir) :
    os.chdir(venv_dir)

q1 = os.listdir()


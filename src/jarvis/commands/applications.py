import subprocess


def open_chrome():
    subprocess.Popen("start chrome", shell=True)
    print("JARVIS: Abriendo Google Chrome.")
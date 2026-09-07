import subprocess


def open_chrome():
    subprocess.Popen("start chrome", shell=True)
    print("JARVIS: Abriendo Google Chrome.")


def open_notepad():
    subprocess.Popen("notepad.exe")
    print("JARVIS: Abriendo el Bloc de notas.")


def open_calculator():
    subprocess.Popen("calc.exe")
    print("JARVIS: Abriendo la calculadora.")
import subprocess


def open_chrome():
    subprocess.Popen("start chrome", shell=True)
    return "Abriendo Google Chrome."

def close_chrome():
    subprocess.run(
        ["taskkill", "/IM", "chrome.exe", "/F"],
        capture_output=True,
        text=True,
    )

    return "Cerrando Google Chrome."

def open_notepad():
    subprocess.Popen("notepad.exe")
    return "Abriendo el Bloc de notas."


def open_calculator():
    subprocess.Popen("calc.exe")
    return "Abriendo la calculadora."


def close_calculator():
    subprocess.run(
        ["taskkill", "/IM", "CalculatorApp.exe", "/F"],
        capture_output=True,
        text=True,
    )

    return "Cerrando la calculadora."
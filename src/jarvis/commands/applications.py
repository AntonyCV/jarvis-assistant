import subprocess

def close_process(process_name):
    subprocess.run(
        ["taskkill", "/IM", process_name, "/F"],
        capture_output=True,
        text=True,
    )

def open_chrome():
    subprocess.Popen("start chrome", shell=True)
    return "Abriendo Google Chrome."

def close_chrome():
    close_process("chrome.exe")
    return "Cerrando Google Chrome."

def open_notepad():
    subprocess.Popen("notepad.exe")
    return "Abriendo el Bloc de notas."

def close_notepad():
    close_process("notepad.exe")
    return "Cerrando el Bloc de notas."

def open_calculator():
    subprocess.Popen("calc.exe")
    return "Abriendo la calculadora."


def close_calculator():
    close_process("CalculatorApp.exe")
    return "Cerrando la calculadora."
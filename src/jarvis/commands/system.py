from datetime import datetime


def say_hello():
    print("JARVIS: Hola. ¿En qué puedo ayudarte?")


def show_time():
    current_time = datetime.now().strftime("%H:%M")
    print(f"JARVIS: Son las {current_time}.")


def show_date():
    current_date = datetime.now().strftime("%d/%m/%Y")
    print(f"JARVIS: Hoy es {current_date}.")
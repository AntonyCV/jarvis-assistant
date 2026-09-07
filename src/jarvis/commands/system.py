from datetime import datetime


def show_time():
    current_time = datetime.now().strftime("%H:%M")
    print(f"JARVIS: Son las {current_time}.")


def say_hello():
    print("JARVIS: Hola. ¿En qué puedo ayudarte?")
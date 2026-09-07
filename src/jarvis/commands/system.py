from datetime import datetime


def say_hello():
    return "Hola. ¿En qué puedo ayudarte?"


def show_time():
    current_time = datetime.now().strftime("%H:%M")
    return f"Son las {current_time}."


def show_date():
    current_date = datetime.now().strftime("%d/%m/%Y")
    return f"Hoy es {current_date}."
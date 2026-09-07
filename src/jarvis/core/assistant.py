from jarvis.core.state import JarvisState
from jarvis.commands.registry import CommandRegistry
from jarvis.commands.interpreter import CommandInterpreter

from jarvis.commands.system import say_hello, show_time, show_date
from jarvis.commands.applications import (
    open_chrome,
    open_notepad,
    open_calculator,
)


class JarvisAssistant:
    def __init__(self):
        self.state = JarvisState()
        self.registry = CommandRegistry()
        self.interpreter = CommandInterpreter()

        self.register_commands()

    def register_commands(self):
        self.registry.register("hola", say_hello)
        self.registry.register("hora", show_time)
        self.registry.register("fecha", show_date)

        self.registry.register("chrome", open_chrome)
        self.registry.register("notepad", open_notepad)
        self.registry.register("calculadora", open_calculator)

    def start(self):
        print("Iniciando JARVIS...")
        print("JARVIS está activo.")
        print()

        while self.state.active:
            user_input = input("Tú: ").strip()

            if user_input.lower() == "salir":
                self.stop()
                continue

            command = self.interpreter.interpret(user_input)

            if command is None:
                print("JARVIS: No entendí lo que dijiste.")
                continue

            if not self.registry.execute(command):
                print("JARVIS: No conozco ese comando.")

    def stop(self):
        print("JARVIS: Cerrando JARVIS...")
        self.state.deactivate()
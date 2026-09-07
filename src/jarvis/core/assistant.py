from jarvis.core.state import JarvisState
from jarvis.commands.registry import CommandRegistry
from jarvis.commands.system import show_time, say_hello
from jarvis.commands.applications import open_chrome


class JarvisAssistant:
    def __init__(self):
        self.state = JarvisState()
        self.registry = CommandRegistry()

        self.register_commands()

    def register_commands(self):
        self.registry.register("hola", say_hello)
        self.registry.register("hora", show_time)
        self.registry.register("chrome", open_chrome)

    def start(self):
        print("Iniciando JARVIS...")
        print("JARVIS está activo.")
        print()

        while self.state.active:
            command = input("Tú: ").strip().lower()

            if command == "salir":
                self.stop()
                continue

            if not self.registry.execute(command):
                print("JARVIS: No conozco ese comando.")

    def stop(self):
        print("JARVIS: Cerrando JARVIS...")
        self.state.deactivate()
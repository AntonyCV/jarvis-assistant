from jarvis.core.state import JarvisState


class JarvisAssistant:
    def __init__(self):
        self.state = JarvisState()

    def start(self):
        print("Iniciando JARVIS...")
        print("JARVIS está activo.")
        print()

        while self.state.active:
            command = input("Tú: ").strip().lower()

            if command == "salir":
                self.stop()

            elif command == "hola":
                self.respond("Hola. ¿En qué puedo ayudarte?")

            else:
                self.respond("No entendí ese comando.")

    def respond(self, message):
        print(f"JARVIS: {message}")

    def stop(self):
        self.respond("Cerrando JARVIS...")
        self.state.deactivate()
        
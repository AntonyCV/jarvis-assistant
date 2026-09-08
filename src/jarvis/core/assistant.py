from jarvis.core.state import JarvisState
from jarvis.commands.registry import CommandRegistry
from jarvis.commands.interpreter import CommandInterpreter
from jarvis.voice.listener import VoiceListener
from jarvis.voice.speaker import VoiceSpeaker

from jarvis.commands.system import say_hello, show_time, show_date
from jarvis.commands.applications import (
    open_chrome,
    close_chrome,
    open_notepad,
    close_notepad,
    open_calculator,
    close_calculator,
)


class JarvisAssistant:
    def __init__(self):
        self.state = JarvisState()
        self.registry = CommandRegistry()
        self.interpreter = CommandInterpreter()
        self.voice_listener = VoiceListener()
        self.voice_speaker = VoiceSpeaker()

        self.register_commands()

    def register_commands(self):
        self.registry.register("simple", "hola", say_hello)
        self.registry.register("simple", "hora", show_time)
        self.registry.register("simple", "fecha", show_date)

        self.registry.register("open", "chrome", open_chrome)
        self.registry.register("close", "chrome", close_chrome)

        self.registry.register("open", "notepad", open_notepad)
        self.registry.register("close", "notepad", close_notepad)
        self.registry.register("open", "calculadora", open_calculator)
        self.registry.register("close", "calculadora", close_calculator)

    def start(self):
        print("Iniciando JARVIS...")
        print("JARVIS está activo.")
        print()

        while self.state.active:
            user_input = self.voice_listener.listen()

            if not user_input:
                continue

            print(f"Tú: {user_input}")

            normalized_input = self.interpreter.normalize(user_input)
            words = normalized_input.split()

            if "jarvis" not in words:
                continue

            jarvis_index = words.index("jarvis")

            command_words = words[jarvis_index + 1:]

            if not command_words:
                self.voice_speaker.speak("Te escucho.")
                continue

            command_text = " ".join(command_words)

            if command_text == "salir":
                self.stop()
                continue

            intent = self.interpreter.interpret(command_text)

            if intent is None:
                self.voice_speaker.speak("No entendí lo que dijiste.")
                continue

            if intent["type"] == "command":
                response = self.registry.execute(
                    "simple",
                    intent["command"],
                )

            elif intent["type"] == "application":
                response = self.registry.execute(
                    intent["action"],
                    intent["application"],
                )

            else:
                response = None

            if response is None:
                self.voice_speaker.speak("No conozco ese comando.")
                continue

            self.voice_speaker.speak(response)

    def stop(self):
        print("JARVIS: Cerrando JARVIS...")
        self.state.deactivate()

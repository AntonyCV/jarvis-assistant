import re
import unicodedata


class CommandInterpreter:
    def __init__(self):
        self.applications = {
            "chrome": "chrome",
            "navegador": "chrome",
            "google": "chrome",

            "calculadora": "calculadora",

            "notepad": "notepad",
            "bloc de notas": "notepad",
            "bloque de notas": "notepad",
        }

        self.actions = {
            # Abrir
            "abrir": "open",
            "abre": "open",
            "abrime": "open",
            "abreme": "open",
            "abras": "open",
            "abres" : "open",

            # Cerrar
            "cerrar": "close",
            "cierra": "close",
            "cierro": "close",
            "cierras": "close",
            "cierres": "close",
}

        self.corrections = {
            "dirime": "dime",
            "dijime": "dime",
            "sierra": "cierra",
            "blog": "bloc",
            "saliro": "salir",

        }

        self.simple_commands = {
            "hola": "hola",
            "buenas": "hola",
            "hey": "hola",

            "hora": "hora",
            "que hora es": "hora",
            "dime la hora": "hora",
            "dime que hora es": "hora",

            "fecha": "fecha",
            "que fecha es": "fecha",
            "que dia es": "fecha",
            "dime la fecha": "fecha",
            "dime que dia es": "fecha",
        }

    def normalize(self, text):
        text = text.lower().strip()

        text = re.sub(r"[^\w\sáéíóúüñ]", "", text)

        text = unicodedata.normalize("NFD", text)
        text = "".join(
            char for char in text
            if unicodedata.category(char) != "Mn"
        )

        text = re.sub(r"\s+", " ", text)

        for wrong, correct in self.corrections.items():
            text = text.replace(wrong, correct)

        return text.strip()

    def interpret(self, text):
        text = self.normalize(text)

        # Comandos simples
        if text in self.simple_commands:
            return {
                "type": "command",
                "command": self.simple_commands[text],
            }

        words = text.split()

        action = None
        application = None

        # Detectar acción
        for word in words:
            if word in self.actions:
                action = self.actions[word]
                break

        # Detectar aplicación
        for application_name, application_id in self.applications.items():
            application_words = application_name.split()

            if self._contains_phrase(words, application_words):
                application = application_id
                break

        if action is None or application is None:
            return None

        return {
            "type": "application",
            "action": action,
            "application": application,
        }

    def _contains_phrase(self, words, phrase_words):
        phrase_length = len(phrase_words)

        for i in range(len(words) - phrase_length + 1):
            if words[i:i + phrase_length] == phrase_words:
                return True

        return False
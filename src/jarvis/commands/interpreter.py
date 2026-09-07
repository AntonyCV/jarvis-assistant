import re
import unicodedata


class CommandInterpreter:
    def __init__(self):
        self.aliases = {
            # Saludos
            "hola": "hola",
            "buenas": "hola",
            "hey": "hola",

            # Hora
            "hora": "hora",
            "que hora es": "hora",
            "dime la hora": "hora",
            "dime que hora es": "hora",
            "que horas": "hora",

            # Fecha
            "fecha": "fecha",
            "que fecha es": "fecha",
            "que dia es": "fecha",
            "dime la fecha": "fecha",
            "dime que dia es": "fecha",

            # Chrome
            "chrome": "chrome",
            "abre chrome": "chrome",
            "abrir chrome": "chrome",
            "abre el navegador": "chrome",
            "abrir el navegador": "chrome",
            "abrime el navegador": "chrome",
            "abre google": "chrome",

            # Bloc de notas
            "notepad": "notepad",
            "bloc de notas": "notepad",
            "bloque de notas": "notepad",
            "abre el bloc de notas": "notepad",
            "abrir el bloc de notas": "notepad",
            "abrime el bloc de notas": "notepad",
            "abre el bloque de notas": "notepad",
            "abrir el bloque de notas": "notepad",

            # Calculadora
            "calculadora": "calculadora",
            "abre la calculadora": "calculadora",
            "abrir la calculadora": "calculadora",
            "abrime la calculadora": "calculadora",

            # Cerrar calculadora
            "cierra la calculadora": "cerrar_calculadora",
            "cerrar la calculadora": "cerrar_calculadora",
            "cierra calculadora": "cerrar_calculadora",
            "cerrar calculadora": "cerrar_calculadora",
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

        return text.strip()

    def interpret(self, text):
        text = self.normalize(text)

        # Primero buscamos coincidencias exactas
        if text in self.aliases:
            return self.aliases[text]

        # Después buscamos frases completas dentro de la oración
        # Solo se permiten aliases de más de una palabra.
        words = text.split()

        for phrase, command in self.aliases.items():
            phrase_words = phrase.split()

            if len(phrase_words) > 1:
                if self._contains_phrase(words, phrase_words):
                    return command

        return None

    def _contains_phrase(self, words, phrase_words):
        phrase_length = len(phrase_words)

        for i in range(len(words) - phrase_length + 1):
            if words[i:i + phrase_length] == phrase_words:
                return True

        return False
class CommandInterpreter:
    def __init__(self):
        self.aliases = {
            "hola": "hola",
            "buenas": "hola",
            "hey": "hola",

            "hora": "hora",
            "qué hora es": "hora",
            "que hora es": "hora",

            "fecha": "fecha",
            "qué fecha es": "fecha",
            "que fecha es": "fecha",

            "chrome": "chrome",
            "abre chrome": "chrome",
            "abrir chrome": "chrome",
            "abre el navegador": "chrome",

            "notepad": "notepad",
            "bloc de notas": "notepad",
            "abre el bloc de notas": "notepad",

            "calculadora": "calculadora",
            "abre la calculadora": "calculadora",
        }

    def interpret(self, text):
        text = text.strip().lower()

        if text in self.aliases:
            return self.aliases[text]

        for phrase, command in self.aliases.items():
            if phrase in text:
                return command

        return None
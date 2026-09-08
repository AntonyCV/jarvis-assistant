from google import genai


class GeminiInterpreter:
    def __init__(self):
        self.client = genai.Client()
        self.model = "gemini-3.5-flash-lite"

    def interpret(self, text):
        prompt = f"""
Eres el intérprete de comandos de un asistente de escritorio llamado JARVIS.

Tu única función es interpretar la intención del usuario.

NO debes ejecutar comandos.
NO debes inventar aplicaciones.
NO debes devolver explicaciones.

Debes responder únicamente con JSON válido.

Acciones permitidas:
- open
- close

Aplicaciones permitidas:
- chrome
- notepad
- calculadora

Ejemplos:

Usuario: abre el navegador
Respuesta:
{{"action": "open", "application": "chrome"}}

Usuario: cierra Chrome
Respuesta:
{{"action": "close", "application": "chrome"}}

Usuario: quiero abrir la calculadora
Respuesta:
{{"action": "open", "application": "calculadora"}}

Usuario: {text}
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text
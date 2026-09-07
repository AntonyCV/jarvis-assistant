import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel


SAMPLE_RATE = 16000
DEVICE = 1


print("Cargando Whisper...")
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8",
)

print("Modelo cargado.")
print()
print("Habla durante 5 segundos.")
print("Di exactamente:")
print("  Hola JARVIS, ¿qué hora es?")
print()

input("Presiona ENTER para comenzar...")

audio = sd.rec(
    int(5 * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="float32",
    device=DEVICE,
)

sd.wait()

audio = np.squeeze(audio)

print()
print("Audio capturado.")
print("RMS:", np.sqrt(np.mean(audio**2)))
print("MAX:", np.max(np.abs(audio)))
print()
print("Transcribiendo...")

segments, info = model.transcribe(
    audio,
    language="es",
    beam_size=5,
    vad_filter=True,
    initial_prompt="JARVIS es el nombre de este asistente de voz.",
)

text = " ".join(
    segment.text.strip()
    for segment in segments
).strip()

print()
print("RESULTADO:")
print(text)
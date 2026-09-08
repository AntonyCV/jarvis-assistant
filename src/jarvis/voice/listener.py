import time
from collections import deque

import numpy as np
import sounddevice as sd

from faster_whisper import WhisperModel


class VoiceListener:
    def __init__(
        self,
        sample_rate=16000,
        silence_threshold=0.01,
        silence_duration=1.2,
        max_duration=8,
        pre_buffer_duration=0.5,
    ):
        self.sample_rate = sample_rate
        self.silence_threshold = silence_threshold
        self.silence_duration = silence_duration
        self.max_duration = max_duration
        self.pre_buffer_duration = pre_buffer_duration

        print("JARVIS: Cargando modelo de reconocimiento de voz...")

        self.model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8",
        )

        print("JARVIS: Modelo cargado correctamente.")

    def listen(self):
        print("JARVIS: Escuchando...")

        audio_chunks = []
        speech_detected = False
        silence_start = None

        pre_buffer_size = int(
            self.pre_buffer_duration * self.sample_rate / 1024
        )

        pre_buffer = deque(maxlen=pre_buffer_size)

        start_time = time.time()

        with sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            dtype="float32",
            blocksize=1024,
            device=1,
        ) as stream:

            while True:
                audio, _ = stream.read(1024)
                audio = np.squeeze(audio)

                volume = np.sqrt(np.mean(audio**2))

                if not speech_detected:
                    pre_buffer.append(audio.copy())

                if volume > self.silence_threshold:
                    if not speech_detected:
                        audio_chunks.extend(pre_buffer)

                    speech_detected = True
                    silence_start = None
                    audio_chunks.append(audio.copy())

                elif speech_detected:
                    audio_chunks.append(audio.copy())

                    if silence_start is None:
                        silence_start = time.time()

                    if time.time() - silence_start >= self.silence_duration:
                        break

                if time.time() - start_time >= self.max_duration:
                    break

        if not speech_detected:
            return ""

        audio_data = np.concatenate(audio_chunks)

        print("JARVIS: Procesando voz...")

        segments, info = self.model.transcribe(
            audio_data,
            language="es",
            beam_size=5,
            vad_filter=True,
        )

        text = " ".join(
            segment.text.strip()
            for segment in segments
        ).strip()

        return text
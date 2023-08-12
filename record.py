# Records a sample from an audio input and saves it to a relative .wav file for shazamio to identify

import pyaudio
import wave

def record_clip(length, file_path, input_device_index):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=input_device_index)

    print("Sampling...")

    frames = []

    for i in range(0, int(RATE / CHUNK * length)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Done sampling.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(file_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
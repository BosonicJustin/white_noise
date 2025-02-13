import pyaudio
import numpy as np

def play_white_noise(volume=0.1, sample_rate=44100, chunk_size=1024):
    p = pyaudio.PyAudio()

    # Open a stream with 1 channel (mono), 32-bit float samples.
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    try:
        print("Playing white noise. Press Ctrl+C to stop.")
        while True:
            # Generate a chunk of random samples between -1.0 and 1.0
            samples = (2 * np.random.random(chunk_size) - 1).astype(np.float32)

            # Adjust for volume
            samples *= volume

            # Convert to bytes and write to the audio stream
            stream.write(samples.tobytes())

    except KeyboardInterrupt:
        print("\nStopping...")

    finally:
        # Properly close the stream
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    play_white_noise(volume=0.1, sample_rate=96000, chunk_size=1024)

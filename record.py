import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

# starts Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
print "Please say something......"
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print "Thank you for Input"

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open('C:/Users/Varun/Desktop/New folder (7)/file.wav', 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

play=pyaudio.PyAudio()
stream_play=play.open(format=FORMAT,
                      channels=CHANNELS,
                      rate=RATE,
                      output=True)

#Gives Output of recording
for data in frames:
    stream_play.write(data)
stream_play.stop_stream()
stream_play.close()
play.terminate()
import pyaudio
import os
import wave
import time

FORMAT = pyaudio.paInt16

# Keep number of channel one to avoid errors in speech api like retry error
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "file.wav"
FLAC_OUTPUT_FILENAME = 'file.flac'
PATH_TO_AUDIO_FILE = os.path.dirname(os.path.abspath(__file__))
frames = []
record_on = False


def callback(in_data, frame_count, time_info, status):
    if record_on:
        global frames
        frames.append(in_data)
        callback_flag = pyaudio.paContinue
    else:
        callback_flag = pyaudio.paComplete

    return (in_data, callback_flag)


def record_audio():
    global frames
    frames = []
    audio = pyaudio.PyAudio()


    '''    
    #start recording without callback
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Please say something......")    
    while record_on:
        data = stream.read(CHUNK)
        frames.append(data)
    '''

    # starts Recording with callback
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK,
                        stream_callback=callback)

    print("Please say something......")
    stream.start_stream()
    
    while stream.is_active():
        time.sleep(0.1)
    
    print("Thank you for Input")
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # get current directory and save recorded file in that directory
    path = PATH_TO_AUDIO_FILE
    path = path + '\\' + WAVE_OUTPUT_FILENAME
    print(path)
    waveFile = wave.open(path, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    """
    play = pyaudio.PyAudio()
    stream_play = play.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            output=True)

    # Gives Output of recording
    for data in frames:
        stream_play.write(data)
    stream_play.stop_stream()
    stream_play.close()
    play.terminate()
    """


def set_path_to_audio_file(path):
    global PATH_TO_AUDIO_FILE
    PATH_TO_AUDIO_FILE = path


# executes this code if script is executed directly in cmd or pycharm
if __name__ == "__main__":
    record_on = True
    record_audio()
    time.sleep(5)
    record_on = False
    pass
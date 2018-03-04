import io
import os
import base64

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# not necessary as for now
def encode_audio(audio):
    audio_content = audio.read()
    return base64.b64encode(audio_content)

def speech_to_text():
    from record import RATE
    from record import WAVE_OUTPUT_FILENAME
    from record import FLAC_OUTPUT_FILENAME
    from record import PATH_TO_AUDIO_FILE

    # location to the json key file. Replace with your location
    json_key_file = "D:\\anurag\Audio to sign language translator\Sign Language Translator-c72c78bbb40e.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_key_file
    print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

    client = speech.SpeechClient()

    # if this script is run from blender, specify the path of audio file that is to be converted into flac
    # PATH_TO_AUDIO_FILE points to current directory. Audio file is saved in that path.
    path = PATH_TO_AUDIO_FILE
    print(path)
    input_file = path + '\\' + WAVE_OUTPUT_FILENAME
    output_file = path + '\\' + FLAC_OUTPUT_FILENAME

    # another approach for converting wav to flac
    """
    conversion_command = 'ffmpeg -ac 1 -i' + input_file + ' ' + output_file
    import subprocess
    p = subprocess.Popen(conversion_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p_out, p_err = p.communicate()
    """

    # convert wav to flac. Be sure that ffmpeg is installed and added to environmental
    # variable path. Restart pycharm after installing.If not working than execute script from cmd.
    try:
        from pydub import AudioSegment
        song = AudioSegment.from_wav(input_file)
        song.export(output_file, format="flac")
    except:
        print("Conversion Failed.")
        print("Make sure ffmpeg is installed and added to environment variable.")
        print("And try running script from cmd instead of pycharm.")
        return

    # read audio file
    with io.open(output_file, 'rb') as audio_file:
        content = audio_file.read()

    # number of channel in audio should be 1 for both wav file and flac file
    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=RATE,
        language_code='en-US')

    response = client.recognize(config, audio)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print('Transcript: {}'.format(result.alternatives[0].transcript))
    print("Finished")

# executes this code if script is executed directly in cmd or pycharm
if __name__ == "__main__":
    speech_to_text()
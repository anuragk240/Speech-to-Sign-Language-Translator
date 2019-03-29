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

def get_client():
    return speech.SpeechClient()


def speech_to_text():
    from recordSpeech import RATE
    from recordSpeech import WAVE_OUTPUT_FILENAME
    from recordSpeech import FLAC_OUTPUT_FILENAME
    from recordSpeech import PATH_TO_AUDIO_FILE

    client = get_client()

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
        import traceback
        from pydub import AudioSegment
        song = AudioSegment.from_wav(input_file)
        song.export(output_file, format="flac")
    except:
        traceback.print_exc()
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
    ans=""
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        ans=result.alternatives[0].transcript
        print('Transcript: {}'.format(result.alternatives[0].transcript))
    print("Finished")
    
    return ans

# executes this code if script is executed directly in cmd or pycharm
if __name__ == "__main__":
    speech_to_text()
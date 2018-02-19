import io
import os
import base64



from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:\\anurag\Audio to sign language translator\Sign Language Translator-c72c78bbb40e.json"
print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

client = speech.SpeechClient()


def encode_audio(audio):
 audio_content = audio.read()
 return base64.b64encode(audio_content)


file="C:/Users/Varun/Desktop/New folder (7)/audio2.raw"



with io.open(file, 'rb') as audio_file:
  content = audio_file.read()


audio = types.RecognitionAudio(content=content)
config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US')

response = client.recognize(config, audio)
# Each result is for a consecutive portion of the audio. Iterate through
# them to get the transcripts for the entire audio file.
for result in response.results:
    # The first alternative is the most likely one for this portion.
    print('Transcript: {}'.format(result.alternatives[0].transcript))


import io
import os

# Imports the Google Cloud client library
from google.cloud import speech, storage
from google.cloud.speech import enums
from google.cloud.speech import types

# ------------Testing google speech api------------------------------#

# set GOOGLE_APPLICATION_CREDENTIALS variable to service credential file path
# set the path to directory where service credential file is present
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:\\anurag\Audio to sign language translator\Sign Language Translator-c72c78bbb40e.json"
print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

# Instantiates a client
client = speech.SpeechClient()

# test audio file uri
gcs_uri = "gs://cloud-samples-tests/speech/brooklyn.flac"
audio = types.RecognitionAudio(uri=gcs_uri)

config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
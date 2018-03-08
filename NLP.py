import os

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/Varun/Desktop/Sign Language Translator-87ce12c513f9.json"
print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])



# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze, only text is given as input to API
text = 'Text only'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

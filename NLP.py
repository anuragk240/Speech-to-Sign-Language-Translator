import os
import six

# Imports the Google Cloud client library

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from NLP_Constants import *

def syntax_text(text):
    """Detects syntax in the text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        language='en',
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects syntax in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML

    response = client.analyze_syntax(document, encoding_type="UTF8")
    sentences = response.sentences
    tokens = response.tokens

    print(u'{:>15} {:>5} {:>15} {:>15} {:>8} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15}'.format("Text",
            "Offset", "Lemma", "dependecy", "POS_TAG", "Number", "Person", "Gender", "Tense", "Aspect", "Mood",
            "Voice", "Proper", "Reciprocity"))
    index = 0
    for sentence in sentences:
        content = sentence.text.content
        sentence_begin = sentence.text.begin_offset
        sentence_end = sentence_begin + len(content) - 1
        while index < len(tokens) and tokens[index].text.begin_offset <= sentence_end:
            # This token is in this sentence
            token = tokens[index]
            print(u'{:>15} {:>5} {:>15} {:>15} {:>8} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15}'.format(
                token.text.content,
                token.text.begin_offset,
                token.lemma,
                dependency_label[token.dependency_edge.label],
                pos_tag[token.part_of_speech.tag],
                pos_number[token.part_of_speech.number],
                pos_person[token.part_of_speech.person],
                pos_gender[token.part_of_speech.gender],
                pos_tense[token.part_of_speech.tense],
                pos_aspect[token.part_of_speech.aspect],
                pos_mood[token.part_of_speech.mood],
                pos_voice[token.part_of_speech.voice],
                pos_proper[token.part_of_speech.proper],
                pos_reciprocity[token.part_of_speech.reciprocity]))
            index += 1



if __name__ == "__main__":
    print("Enter text.")
    text = input()
    syntax_text(text)
    pass
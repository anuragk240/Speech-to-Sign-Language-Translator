import os
import six

# Imports the Google Cloud client library

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from NLP_Constants import *


def get_client():
    return language.LanguageServiceClient()


def syntax_text(text):
    """Detects syntax in the text."""

    client = get_client()

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

    printHeaders()
    gloss = []

    index = 0
    for sentence in sentences:
        content = sentence.text.content
        sentence_begin = sentence.text.begin_offset
        sentence_end = sentence_begin + len(content) - 1
        while index < len(tokens) and tokens[index].text.begin_offset <= sentence_end:
            # This token is in this sentence
            token = tokens[index]

            # handle cases for different POS tags
            switch(pos_tag[token.part_of_speech.tag], token, gloss)

            printToken(token)
            index += 1
    print(gloss)
    return gloss


def processVerb(token, gloss):
    pass


def processNoun(token, gloss):
    if pos_proper[token.part_of_speech.proper] == 'PROPER':
        # noun is proper. Need fingerspelling. Split it into alphabets
        fingerspell = ['Alphabet.' + s.upper() for s in list(token.text.content)]
        gloss.extend(fingerspell)
    else:
        # it is a common noun
        gloss.append(token.lemma.lower())


def doNothing(token, gloss):
    pass


def default(token, gloss):
    # returns base word of token
    return gloss.append(token.lemma.lower())


# a switch function that processes each token according to the pos tag of that token
# and calls suitable function to handle that token
def switch(tag, token, gloss):
    switcher = {
        'ADJ': default,
        'ADP': default,
        'ADV': default,
        'CONJ': default,
        'DET': default,
        'NOUN': processNoun,
        'NUM': default,
        'PRON': default,
        'PRT': default,
        'VERB': default,
        'AFFIX': default,
        'PUNCT': doNothing,
        'X': doNothing,
        'UNKNOWN': default
    }
    fun = switcher.get(tag, default)
    # call the function
    fun(token, gloss)


# utils functions for printing data obtained from NLP API----------------------------
def printHeaders():
    print(u'{:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15}'.format("Text",
                                                                                          "Lemma", "dependecy",
                                                                                          "head_index", "POS_TAG",
                                                                                          "Number", "Person", "Gender",
                                                                                          "Tense", "Proper"))


def printToken(token):
    print(u'{:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15}'.format(
        token.text.content,
        token.lemma,
        dependency_label[token.dependency_edge.label],
        token.dependency_edge.head_token_index,
        pos_tag[token.part_of_speech.tag],
        pos_number[token.part_of_speech.number],
        pos_person[token.part_of_speech.person],
        pos_gender[token.part_of_speech.gender],
        pos_tense[token.part_of_speech.tense],
        # pos_aspect[token.part_of_speech.aspect],
        # pos_mood[token.part_of_speech.mood],
        # pos_voice[token.part_of_speech.voice],
        pos_proper[token.part_of_speech.proper]
        # pos_reciprocity[token.part_of_speech.reciprocity]
    ))


# for testing
if __name__ == "__main__":
    print("Enter text.")
    text = input()
    gloss = syntax_text(text)
    pass
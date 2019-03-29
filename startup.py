import bge
import recordSpeech
import threading
import Speechtotext
import NLP
import playAnimations
import os

start_animation = False
action_num = 0
actions = []
text_obj = None
gloss = None
con_obj = None

# background thread for recording and other stuff
def run():
    print("Starting worker")
    
    # start recording
    recordSpeech.record_audio()
    global text_obj, con_object, actions, start_animation, action_num, thread
    text_obj.text = "Converting Speech to Text"
    
    # convert speech to text
    text = Speechtotext.speech_to_text().lower()
    #text = "Test text"
    
    con_obj.visible=True
    con_obj.text = "Speech: " + text.upper()
    
    text_obj.text = "Analysing Syntax"

    # TODO:convert text to gloss form
    # dummy code- gets base word for each word and returns the array as gloss array
    gloss_array = NLP.syntax_text(text)
    
    # play animations sequentially
    text_obj.text = "Animating"
    
    actions = playAnimations.get_actions(gloss_array)
    start_animation = True
    global gloss
    gloss.visible = True
    action_num = 0
    print("Finished worker")
    thread=None


thread = None

def main():
    # main logic for updating blender ui and other things
    # print("recording ", thread.isAlive())
    
    if start_animation:
        global action_num, text_obj
        text_obj.text = "Animating"
        action_num = playAnimations.play_animation(actions, action_num)
        pass
    pass


# call this when r is pressed
# this starts a new thread for recording
def start_thread():
    sens = bge.logic.getCurrentController().sensors['record']
    if sens.positive:
        print("R pressed")
        if thread is None:
            global thread
            thread = threading.Thread(target=run)

        if not thread.isAlive():
            print("initialised thread")
            
            print("path")
            path = bge.logic.expandPath("//")
            print(path)
            recordSpeech.set_path_to_audio_file(path)
            
            recordSpeech.record_on = True
            thread.start()
            global text_obj
            text_obj.text = "Stop Recording (S)"
            print("thread started")


def stop_recording():
    sens = bge.logic.getCurrentController().sensors['stop_record']
    if sens.positive:
        if thread is not None and thread.isAlive() and recordSpeech.record_on:
            print("terminating recording")
            # global text_obj
            # text_obj.text = "Playing audio"
            recordSpeech.record_on = False
        else:
            print("thread none or not running")


def init():
    # initialise
    global text_obj, gloss, con_obj
    
    text_obj = bge.logic.getCurrentScene().objects['Text']
    text_obj.text = "Record Speech (R)"
    text_obj.resolution = 8.0
    
    gloss = bge.logic.getCurrentScene().objects['gloss']
    gloss.resolution = 8.0
    
    con_obj = bge.logic.getCurrentScene().objects['converted_text']
    con_obj.resolution = 8.0
    
    # location to the json key file. Replace with your location
#    json_key_file = "E:\\anurag\Audio to sign language translator\sign-language-translator-02ff41a913bf.json"
 #   os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_key_file
  #  print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
    
    # get clients for nlp and speech
    Speechtotext.get_client()
    NLP.get_client()
    
    # read animation data from txt file
    import json
    path = bge.logic.expandPath("//")
    path = path + "\\animationData.txt"
    playAnimations.animationList = json.load(open(path))
    
    print("init")
    
def exit():
    print("exiting bge")
    # check if thread is running, wait for it to stop.
    if thread is not None and thread.isAlive():
        if recordSpeech.record_on:
            recordSpeech.record_on = False
        print("waiting for thread to stop")
        thread.join()

# for testing
if __name__ == "__main__":
    # ensure that this code is run only one time when sensor is activated
    # sens = bge.logic.getCurrentController().sensors['startup']
    # if sens.positive:
    print("test")
    pass

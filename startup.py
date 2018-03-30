import bge
import recordSpeech
import threading
import Speechtotext
import NLP
import playAnimations

start_animation = False
action_num = 0
actions = []
text_obj = None
gloss = None

# background thread for recording and other stuff
def run():
    print("Starting worker")

    # start recording
    recordSpeech.record_audio()
    global text_obj
    text_obj.text = "Converting Speech to Text"

    # convert speech to text
    text = "happy new year"
    text = Speechtotext.speech_to_text()
    con_obj = bge.logic.getCurrentScene().objects['converted_text']
    con_obj.visible = True
    con_obj.text = "Speech: " + text
    con_obj.resolution = 8.0

    # TODO:convert text to gloss form
    # dummy code splits text into words and returns it as gloss array
    gloss_array = text.lower().split()

    # play animations sequentially
    # gloss_array = ['happy', 'new', 'year']
    global text_obj
    text_obj.text = "Animating"

    global actions, start_animation, action_num, thread
    actions = playAnimations.get_actions(gloss_array)
    start_animation = True
    action_num = 0
    print("Finished worker")
    thread = None


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
    global text_obj
    text_obj.text = "Stop Recording (S)"
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
            global is_recording
            print("thread started")


def stop_recording():
    sens = bge.logic.getCurrentController().sensors['stop_record']
    if sens.positive:
        if thread is not None and thread.isAlive():
            print("terminating recording")
            global text_obj
            text_obj.text = "Playing audio"
            recordSpeech.record_on = False
        else:
            print("thread none or not running")


def init():
    # initialise
    global text_obj, gloss
    text_obj = bge.logic.getCurrentScene().objects['Text']
    text_obj.text = "Record Speech (R)"
    text_obj.resolution = 8.0
    gloss = bge.logic.getCurrentScene().objects['gloss']
    gloss.resolution = 8.0
    print("init")

def exit():
    pass

# for testing
if __name__ == "__main__":
    # ensure that this code is run only one time when sensor is activated
    # sens = bge.logic.getCurrentController().sensors['startup']
    # if sens.positive:
    print("test")
    pass

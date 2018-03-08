import bpy
import bge
import recordSpeech
import threading
import Speechtotext

# background thread for recording and other stuff
def run():
    print("Starting worker")
    # start recording
    recordSpeech.record_audio()
    # convert speech to text
    Speechtotext.speech_to_text()
    print("Finished worker")


thread = threading.Thread(target=run)


def main():
    # main logic for updating blender ui and other things
    # print("recording ", thread.isAlive())
    pass


# call this when r is pressed
# this starts a new thread for recording
def start_thread():
    # initialise
    sens = bge.logic.getCurrentController().sensors['record']
    if sens.positive:
        print("path")
        path = bpy.path.abspath("//")
        print(path)
        recordSpeech.set_path_to_audio_file(path)

        print("R pressed")
        if not thread.isAlive():
            recordSpeech.record_on = True
            thread.start()
            print("thread started")


def stop_recording():
    sens = bge.logic.getCurrentController().sensors['stop_record']
    if sens.positive and thread.isAlive():
        print("terminating recording")
        recordSpeech.record_on = False


# for testing
if __name__ == "__main__":
    # ensure that this code is run only one time when sensor is activated
    # sens = bge.logic.getCurrentController().sensors['startup']
    # if sens.positive:
    print("test")


import bge
import startup

animationList = {}


def play_animation(actions, i):
    # get the controller that started this script
    con = bge.logic.getCurrentController()
    obj = con.owner

    # print(obj)

    if obj.isPlayingAction(0):
        return i
    elif i == len(actions):
        startup.start_animation = False
        startup.text_obj.text = "Record Speech (R)"
        startup.con_obj.text = ""
        startup.con_obj.visible = False
        startup.gloss.text = ""
        startup.gloss.visible = False

    else:
        play_action(actions[i])
        if not actions[i][1:] == [0, 0]:
            update_gloss(i, actions[i][0])
        i = i + 1

    return i


def update_gloss(i, action):
    if not action == "RestPose":
        if action[0].isupper():
            # action is of an alphabet
            startup.gloss.text += action[-1]
        else:
            # action is of a word
            startup.gloss.text += action.upper() + " "


def get_actions(gloss_array):
    import json
    actions = []

    # read animation data from file
    path = bge.logic.expandPath("//")
    path = path + "\\animationData.txt"
    animationList = json.load(open(path))

    count = len(gloss_array)
    (start, end) = animationList.get("RestPose", [0, 0])
    actions.append(["RestPose", start, end])

    for i in range(0, count):
        start, end = animationList.get(gloss_array[i], [0, 0])
        actions.append([gloss_array[i], start, end])

    start, end = animationList.get("RestPose", [0, 0])
    actions.append(["RestPose", 0, 6])

    return actions


def play_action(data):
    action = data[0]
    start = data[1]
    end = data[2]
    cont = bge.logic.getCurrentController()
    main_arm = cont.owner
    layer = 0
    priority = 0
    blendin = 3
    mode = 0
    # mode
    # KX_ACTION_MODE_PLAY is 0
    # KX_ACTION_MODE_LOOP is 1
    # etc
    layerWeight = 0.0
    ipoFlags = 0
    speed = 0.8
    print("action played " + action)
    main_arm.playAction(action, start, end, layer, priority, blendin, mode, layerWeight, ipoFlags, speed)


# for testing
if __name__ == "__main__":
    con = bge.logic.getCurrentController()
    sens = con.sensors['Start animation']
    if sens.positive:
        play_animation([])
        # get the game object this controller is on:
        # build_logic_bricks(['A', 'Z', 'J'])
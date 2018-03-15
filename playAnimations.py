import bge
import startup


def play_animation(actions, i):
    # get the controller that started this script
    con = bge.logic.getCurrentController()
    obj = con.owner

    # print(obj)

    if obj.isPlayingAction(0):
        return i
    elif i == len(actions):
        startup.start_animation = False
    else:
        play_action(actions[i])
        i = i + 1

    return i


def get_actions(gloss_array):
    actions = []
    actions.append(["Alphabet." + gloss_array[0], 0, 9])
    count = len(gloss_array) - 1
    for i in range(1, count):
        actions.append(["Alphabet." + gloss_array[i], 5, 9])
    actions.append(["Alphabet." + gloss_array[count], 5, 18])

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
    speed = 0.5
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
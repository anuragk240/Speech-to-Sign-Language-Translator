# setup script to be run before running bge
# This fetches animation data from blender and stores it
# in text file which is read by bge while playing animations in sequence.
import bpy

animationList = {}


def writeAnimationData():
    import json
    # as requested in comment
    path = bpy.path.abspath('//')
    path = path + '\\animationData.txt'
    json.dump(animationList, open(path, 'w'))


def getActionData():
    global animationList
    animationList = {}
    for i in range(len(bpy.data.actions)):
        act = (bpy.data.actions[i].frame_range[0], bpy.data.actions[i].frame_range[1])

        animationList[bpy.data.actions[i].name] = act

    # print(animationList)


if __name__ == "__main__":
    import json

    getActionData()
    writeAnimationData()
    print("file written")
    print(len(animationList))

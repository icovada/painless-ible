import datetime
import json

with open("animations.config", "r") as animationsfile:
    animations = json.loads(animationsfile)

with open("colours.config", "r") as coloursfile:
    colours = json.loads(coloursfile)

with open("calendar.config", "r") as calendarfile:
    calendar = json.loads(calendarfile)

assert "default" in animations.keys()

defaultanimation = animations.pop("default")
animationlist = []

for i, j in animations.items():
    for k in j:
        if k not in animationlist:
            animationlist.append(k)


# Header
header1 = [0x50, 0x48, 0x54, 0x00, 0x00, 0x00, 0x00,
           0x00, 0x31, 0x31, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00]
heaser2 = "1/1/2019/"
header3 = [0x00, 0x00, 0xD9, 0x00, 0x00, 0x00]
fieldseparator = 0x1D

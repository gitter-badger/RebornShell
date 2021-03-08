import random
import rbsh_colors

actions = 1
todo = random.randint(0, actions)

if todo == 0:
    print(rbsh_colors.background_presets["red"].getCode() + "  --<RBSH - ReBornSHell>--  " + rbsh_colors.reset.getCode())
    for x in range(7):
        color = rbsh_colors.Color()
        color.color = 40 + x
        print(color.getCode() + "    ", end=rbsh_colors.reset.getCode())
elif todo == 1:
    print(rbsh_colors.background_presets["red"].getCode() + "       ReBornSHell       " + rbsh_colors.reset.getCode())
    for key, value in rbsh_colors.foreground_presets.items():
        if key != "white":
            print(rbsh_colors.background_presets["white"].getCode() + value.getCode() + "  " + rbsh_colors.reset.getCode(), end="")
    print()

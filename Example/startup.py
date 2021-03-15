import random
import rbsh_colors

actions = 3
todo = random.randint(0, actions)

linux_icons = "                          ".split()
prog_lang_icons = "              ".split()

if todo == 0:
    print(rbsh_colors.background_presets["blue"].getCode() +
          "  --<RBSH - ReBornSHell>--  " +
          rbsh_colors.reset)
    for key, value in rbsh_colors.foreground_presets.items():
        if key != "black":
            print(rbsh_colors.background_presets["black"].getCode() +
                  value.getCode() +
                  "  ",
                  end=rbsh_colors.reset)
    print()

    for x in range(7):
        color = rbsh_colors.Color()
        color.color = 40 + x
        print(color.getCode() + "    ", end=rbsh_colors.reset)

elif todo == 1:
    print(rbsh_colors.background_presets["red"].getCode() +
          "       ReBornSHell       " +
          rbsh_colors.reset)

    for key, value in rbsh_colors.foreground_presets.items():
        if key != "white":
            print(rbsh_colors.background_presets["white"].getCode() +
                  value.getCode() + "  " +
                  rbsh_colors.reset, end="")
    print()

elif todo == 2:
    bg = random.choice(list(rbsh_colors.background_presets.values()))
    for x in range(16):
        while bg == rbsh_colors.background_presets["white"]:
            bg = random.choice(list(rbsh_colors.background_presets.values()))
        print(bg.getCode() +
              " " +
              random.choice(linux_icons) +
              " ",
              end=rbsh_colors.reset)
        bg = random.choice(list(rbsh_colors.background_presets.values()))
    print()

elif todo == 3:
    bg = random.choice(list(rbsh_colors.background_presets.values()))
    for x in range(16):
        while bg == rbsh_colors.background_presets["white"]:
            bg = random.choice(list(rbsh_colors.background_presets.values()))
        print(bg.getCode() +
              " " +
              random.choice(prog_lang_icons) +
              " ",
              end=rbsh_colors.reset)
        bg = random.choice(list(rbsh_colors.background_presets.values()))
    print()

# this is the config for RBSH

import rbsh_colors


# NOTE: Prompt Zone
# what to print at the top, but only when RBSH first starts (Default: nothing)
prompt_onetime_top = ""
# Should the prompt be two lines? (Default: True)
multiline_prompt = False
# What the prompt is (Default: $)
prompt = "$ "
prompt = "ﬦ "


# NOTE: Execution Zone
# what should be used to execute from the `input(prompt)`
# if it's set to nothing then it's just with `os.system()`
# example: command_to_exec_with = "sh -c"
# that would make every command be executed as if it was:
# `sh -c echo 'hello world'`
# default: nothing
command_to_exec_with = ""
# what command should be executed when RBSH first starts (Default: nothing)
first_command_to_exec = "python3 startup.py"
# what command should be executed right before RBSH closes (Default: "echo 'Goodbye!'")
before_closing = "echo 'Goodbye!'"


# NOTE: Colors Zone
# prompt color
prompt_color = rbsh_colors.Color()
prompt_color.bold = 1
# the color of the pwd
pwd_color = rbsh_colors.Color()
pwd_color.color = 91


# NOTE: Symbols zone
# what symbol should represent the home dir (Default: ~)
home_symbol = "~"
home_symbol = ""
# what symbol should represent the / dir (Default: /)
sys_root_symbol = "/"

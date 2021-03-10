# this is the config for RBSH

import rbsh_colors


# NOTE: Prompt Zone
# what to print at the top, but only when RBSH first starts (Default: nothing)
prompt_onetime_top = ""
# Should the prompt be two lines? (Default: True)
multiline_prompt = True
# What the prompt is (Default: $)
prompt = "$ "


# NOTE: Execution Zone
# what should be used to execute from the `input(prompt)`
# if it's set to nothing then it's just with `os.system()`
# example: command_to_exec_with = "sh -c"
# that would make every command be executed as if it was:
# `sh -c echo 'hello world'`
# default: nothing
command_to_exec_with = ""
# what command should be executed when RBSH first starts (Default: nothing)
first_command_to_exec = ""
# what command will be executed before RBSH closes (Default: "echo 'Goodbye!'")
before_closing = "echo 'Goodbye!'"


# NOTE: Colors Zone
# prompt color
prompt_color = rbsh_colors.foreground_presets["blue"]
# the color of the pwd
pwd_color = rbsh_colors.foreground_presets["red"]


# NOTE: Symbols zone
# what symbol should represent the home dir (Default: ~)
home_symbol = "~"
# what symbol should represent the / dir (Default: /)
sys_root_symbol = "/"

# NOTE: Alias zone
# define aliases in this dict
alias_list = {
    # alias: command
    "py": "python3",
    "py2": "python2"
}

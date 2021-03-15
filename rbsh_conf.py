# this is the config for RBSH

import rbsh_colors


# NOTE: Prompt Zone
# what to print at the top, but only when RBSH first starts (Default: nothing)
prompt_onetime_top = ""
# should the prompt be two lines? (Default: True)
multiline_prompt = True
# what the prompt is (Default: $)
prompt = "$ "
# prompt head
prompt_head = rbsh_colors.foreground_presets["magenta"].getCode() + "]" + rbsh_colors.reset
# prompt tail
prompt_tail = rbsh_colors.foreground_presets["magenta"].getCode() + "[" + rbsh_colors.reset
# python venv text
pyvenv_text = rbsh_colors.foreground_presets["blue"].getCode() + "Py" + rbsh_colors.foreground_presets["yellow"].getCode() + "env"
# seperator character (Default: |)
seperator_char = rbsh_colors.foreground_presets["magenta"].getCode() + " | " + rbsh_colors.reset


# NOTE: Execution Zone
# what should be used to execute from the `input(prompt)`
# if it's set to nothing then it's just with `os.system()`
# example: exec_with = "sh -c"
# that would make every command be executed as if it was:
# `sh -c echo 'hello world'`
# default: None
exec_with = None
# what command should be executed when RBSH first starts (Default: None)
first_cmd = None
# what command will be executed before RBSH closes (Default: "echo 'Goodbye!'")
before_closing = "echo Goodbye!"


# NOTE: Colors Zone
# prompt color
prompt_color = rbsh_colors.foreground_presets["blue"].getCode()
# the color of the pwd
pwd_color = rbsh_colors.foreground_presets["red"].getCode()


# NOTE: Symbols zone
# what symbol should represent the home dir (Default: ~)
home_symbol = "~"
# what symbol should represent the / dir (Default: /)
sys_root_symbol = "/"
# what symbol should be used for the "/" parts of a path (Default: /)
path_slash_symbol = "/"


# NOTE: Alias zone
# define aliases in this dict
alias_list = {
    # alias: command
    "py": "python3",
    "py2": "python2"
}

import rbsh_colors

# NOTE: Prompt Zone
prompt_onetime_top = ""
multiline_prompt = False
prompt = (rbsh_colors.foreground_presets["blue"].getCode() +
          "─ﬦ ")
prompt_head = (rbsh_colors.foreground_presets["red"].getCode() +
               "" +
               rbsh_colors.reset)
prompt_tail = (rbsh_colors.foreground_presets["red"].getCode() +
               "" +
               rbsh_colors.reset)
pyvenv_text = (rbsh_colors.background_presets["red"].getCode() +
               rbsh_colors.foreground_presets["blue"].getCode()
               + " " +
               rbsh_colors.foreground_presets["yellow"].getCode() +
               " Pyenv" +
               rbsh_colors.reset +
               rbsh_colors.background_presets["red"].getCode() +
               "")
seperator_char = (rbsh_colors.foreground_presets["red"].getCode() +
                  " " +
                  rbsh_colors.reset)

# NOTE: Execution Zone
exec_with = ""
first_cmd = "python3 /home/imahaxer/.config/RebornShell/startup.py"
before_closing = "echo Goodbye!"


# NOTE: Colors Zone
prompt_color = rbsh_colors.foreground_presets["blue"].getCode()
pwd_color = rbsh_colors.background_presets["red"].getCode()


# NOTE: Symbols zone
home_symbol = "ﴤ"
sys_root_symbol = "ﳎ"
path_slash_symbol = "/"

# NOTE: Alias zone
alias_list = {
    "py": "python3",
    "py2": "python2"
}

import rbsh_colors


# NOTE: Prompt Zone
prompt_onetime_top = ""
multiline_prompt = False
prompt = "ﬦ "


# NOTE: Execution Zone
command_to_exec_with = ""
first_command_to_exec = "python3 ~/.config/RebornShell/startup.py"
before_closing = "echo 'Goodbye!'"


# NOTE: Colors Zone
prompt_color = rbsh_colors.Color()
prompt_color.bold = 1
pwd_color = rbsh_colors.Color()
pwd_color.color = 91


# NOTE: Symbols zone
home_symbol = ""
sys_root_symbol = "/"

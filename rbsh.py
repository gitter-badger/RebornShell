# NOTE: Imports
import os
import sys
import subprocess
import readline
import rbsh_conf
import rbsh_colors


# NOTE: Functions
def get_pwd_colored():
    try:
        pwd = subprocess.check_output("/bin/pwd")
        pwd = pwd.decode("UTF-8").strip("\n")
        result = pwd.replace(os.path.expanduser("~"), rbsh_conf.home_symbol)

        if result == "/":
            result = rbsh_conf.sys_root_symbol

        result = rbsh_conf.pwd_color + result + rbsh_colors.reset

        return result.replace("/", rbsh_conf.path_slash_symbol, 9999)
    except subprocess.CalledProcessError as err:
        print(err)


def get_pwd():
    try:
        pwd = subprocess.check_output("/bin/pwd")
        pwd = pwd.decode("UTF-8").strip("\n")
        return pwd + "/"
    except subprocess.CalledProcessError as err:
        print(err)


def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))


def get_py_venv():
    try:
        if is_venv():
            return rbsh_conf.seperator_char + rbsh_conf.pyvenv_text
        return ""
    except subprocess.CalledProcessError as err:
        print(err)


def execute(toexec):
    # exit
    if toexec == "exit":
        if rbsh_conf.before_closing is not None:
            try:
                subprocess.run(rbsh_conf.before_closing.split(), check=False,
                               shell=False)
            except FileNotFoundError:
                print("RBSH: Error, command not found.")
        sys.exit()

    # cd
    if toexec.startswith("cd"):
        if toexec == "cd":
            os.chdir(os.path.expanduser("~") + "/")
            return

        if toexec == "cd /":
            os.chdir("/")
            return

        if toexec == "cd .":
            os.chdir(".")
            return

        toexec = toexec.replace("cd", "")
        # no idea why, but there was a space always before the dir name
        toexec = toexec.replace(" ", "", 1)
        if not toexec.startswith("/"):
            try:
                print(get_pwd() + toexec)
                os.chdir(get_pwd() + toexec)
            except FileNotFoundError:
                print("Directory not found")
            return
        try:
            os.chdir(toexec)
        except FileNotFoundError:
            print("Directory not found")
        return

    # execute!
    try:
        if rbsh_conf.exec_with is None:
            subprocess.run(toexec.split(), check=False, shell=False)
        else:
            subprocess.run(rbsh_conf.exec_with.split() + toexec.split(),
                           check=False, shell=False)
    except FileNotFoundError:
        print("RBSH: Error, command not found.")


# NOTE: Startup
# print one-time prompt
print(rbsh_conf.prompt_onetime_top)

# execute first_command_to_exec
if rbsh_conf.first_cmd is not None:
    subprocess.run(rbsh_conf.exec_with.split() + rbsh_conf.first_cmd.split(),
                   check=False, shell=False)

# NOTE: Mainloop
while 1:
    # this is getting large...
    # here's the prompt, I'd say you should just leave it alone.
    if rbsh_conf.multiline_prompt:
        prompt = (str(rbsh_conf.prompt_color) +
                  str("\n╭─") +
                  str(rbsh_conf.prompt_tail) +
                  str(get_pwd_colored()) +
                  str(rbsh_colors.reset) +
                  str(get_py_venv()) +
                  str(rbsh_conf.prompt_color) +
                  str(rbsh_conf.prompt_head) +
                  str(rbsh_conf.prompt_color) +
                  str("\n╰─") +
                  str(rbsh_conf.prompt) +
                  str(rbsh_colors.reset)
                  )
    else:
        prompt = (str("\n") +
                  str(rbsh_conf.prompt_color) +
                  str(rbsh_conf.prompt_tail) +
                  str(get_pwd_colored()) +
                  str(rbsh_colors.reset) +
                  str(get_py_venv()) +
                  str(rbsh_conf.prompt_head) +
                  str(rbsh_conf.prompt_color) +
                  str(rbsh_conf.prompt) +
                  str(rbsh_colors.reset)
                  )

    # thank you so much @Zombie_Pigdragon#3468 (Discord) for helping me out!
    # the line below this one is what made everything work great!
    readline.parse_and_bind("")  # no settings
    action = input(prompt)

    # aliases, get over how messy this code is
    new_action = action.split()
    for x in action.split():
        for key, value in rbsh_conf.alias_list.items():
            if x == key:
                new_action[new_action.index(key)] = value
    action = " ".join(action)
    new_action = " ".join(new_action)

    # execute the command
    execute(new_action)

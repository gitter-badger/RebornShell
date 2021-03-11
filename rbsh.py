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

        return rbsh_conf.pwd_color.getCode() + result + rbsh_colors.reset
    except subprocess.CalledProcessError as err:
        print(err)


def get_pwd():
    try:
        pwd = subprocess.check_output("/bin/pwd")
        pwd = pwd.decode("UTF-8").strip("\n")

        return pwd + "/"
    except subprocess.CalledProcessError as err:
        print(err)


def execute(toexec):
    # exit
    if toexec == "exit":
        if rbsh_conf.before_closing is not None:
            subprocess.run(rbsh_conf.before_closing.split(), check=False,
                           shell=False)

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
        toexec = toexec.replace(" ", "")
        if not toexec.startswith("/"):
            try:
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
    if rbsh_conf.exec_with is None:
        subprocess.run(toexec.split(), check=False, shell=False)
    else:
        subprocess.run(rbsh_conf.exec_with.split() + toexec.split(),
                       check=False, shell=False)


# NOTE: Startup
# print one-time prompt
print(rbsh_conf.prompt_onetime_top)

# execute first_command_to_exec
if rbsh_conf.first_cmd is not None:
    subprocess.run(rbsh_conf.exec_with.split() + rbsh_conf.first_cmd.split(),
                   check=False, shell=False)

# NOTE: Mainloop
while 1:
    if rbsh_conf.multiline_prompt:
        prompt = (rbsh_conf.prompt_color.getCode() +
                  "\n╭─[" +
                  get_pwd_colored() +
                  rbsh_conf.prompt_color.getCode() +
                  "]\n╰─" +
                  rbsh_conf.prompt +
                  rbsh_colors.reset
                  )
    else:
        prompt = ("\n" +
                  rbsh_conf.prompt_color.getCode() +
                  "[" +
                  get_pwd_colored() +
                  rbsh_conf.prompt_color.getCode() +
                  "] " +
                  rbsh_conf.prompt +
                  rbsh_colors.reset
                  )

    # thank you so much @Zombie_Pigdragon#3468 (Discord) for helping me out!
    # the line below this one is what made everything work perfectly!
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

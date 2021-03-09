import os
import subprocess
import rbsh_conf
import rbsh_colors


def get_pwd_colored():
    try:
        pwd = subprocess.check_output("pwd")
        pwd = pwd.decode("UTF-8").strip("\n")
        pwd = pwd.replace(os.path.expanduser("~"), rbsh_conf.home_symbol)
        if pwd == "/":
            pwd = rbsh_conf.sys_root_symbol
        return (rbsh_conf.pwd_color.getCode() + pwd +
                rbsh_colors.reset.getCode())
    except subprocess.CalledProcessError as err:
        print(err)


def get_pwd():
    try:
        pwd = subprocess.check_output("pwd")
        pwd = pwd.decode("UTF-8").strip("\n")
        return pwd + "/"
    except subprocess.CalledProcessError as err:
        print(err)


def execute(toexec):
    # exit
    if toexec == "exit":
        if rbsh_conf.before_closing is not None:
            os.system(rbsh_conf.before_closing)
        quit()

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
    if rbsh_conf.command_to_exec_with is None:
        os.system(toexec)
    else:
        os.system(rbsh_conf.command_to_exec_with + toexec)


# print one-time prompt
print(rbsh_conf.prompt_onetime_top)

# execute first_command_to_exec
if rbsh_conf.first_command_to_exec is not None:
    os.system(rbsh_conf.command_to_exec_with + rbsh_conf.first_command_to_exec)

# loop
while 1:
    if rbsh_conf.multiline_prompt:
        execute(input(rbsh_conf.prompt_color.getCode() +
                      "\n╭─[" +
                      get_pwd_colored() +
                      rbsh_conf.prompt_color.getCode() +
                      "]\n╰─" +
                      rbsh_conf.prompt +
                      rbsh_colors.reset.getCode()
                      ))
    elif not rbsh_conf.multiline_prompt:
        execute(input("\n" +
                      rbsh_conf.prompt_color.getCode() +
                      "[" +
                      get_pwd_colored() +
                      rbsh_conf.prompt_color.getCode() +
                      "] " +
                      rbsh_conf.prompt +
                      rbsh_colors.reset.getCode()
                      ))

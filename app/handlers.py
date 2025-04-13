import os
import sys
import shutil

def exit_cmd(args : list[str]):
    sys.exit(0)

def ls_cmd(args : list[str]):
    path = "."
    if args[0] :
        path = args[0]
    for item in os.listdir(path):
        print(item)

def cd_cmd(args : list[str]):
    path = args[0]
    if os.path.isdir(path):
        os.chdir(path)
    else:
        print(f"cd: {path}: No such file or directory")

def pwd_cmd(args : list[str]):
    print(os.getcwd())


def echo_cmd(args : list[str]):
    for arg in args:
        print(arg, end=" ")

def type_cmd(args : list[str]):
    command = args[0]
    from main import SUPPORTED_COMMANDS,get_all_executable_commands
    if command in SUPPORTED_COMMANDS:
        print(f"{command} is a shell builtin")
        return
    executables = get_all_executable_commands()
    if command in executables:
        path_of_command = shutil.which(command)
        print(f"{command} is {path_of_command}")


def clear_cmd(args : list[str]):
    print("\033[H\033[J", end="")  # ANSI escape code to clear the screen





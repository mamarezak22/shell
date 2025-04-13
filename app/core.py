import os
import sys
import socket
import subprocess

from .handlers import (ls_cmd , pwd_cmd , cd_cmd , type_cmd,
exit_cmd , clear_cmd , echo_cmd)
from typing import Callable

SUPPORTED_COMMANDS  = ["ls","pwd","cd","type","exit","clear","echo"]
map_command_to_handler : dict[str,Callable] = {
    "ls" : ls_cmd,
    "pwd" : pwd_cmd,
    "cd" : cd_cmd,
    "type" : type_cmd,
    "exit" : exit_cmd,
    "clear" : clear_cmd,
    "echo" : echo_cmd,
}

def get_all_executable_commands() -> list[str]:
    #in any os os.path seperator is a diffrent char.
    #in linux is : and in windows ;
    path_dirs = os.getenv("PATH","").split(os.pathsep)
    executables = []
    
    for dir in path_dirs:
        if os.path.isdir(dir):
            # Get all files in the directory
            for file_name in os.listdir(dir):
                file_path = os.path.join(dir, file_name)
                
                # Check if it's executable
                if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                    executables.append(file_name)
    return executables

def parse_input(input : str)->tuple[str,list[str]]:
    parts = input.split()
    command = parts[0]
    args = parts[1:]
    return command,args

def run_exe(exe : str, args : list[str]):
    subprocess.run([exe] + args, shell=True)
    
def run_command(command : str , args : list[str]):
    if command in map_command_to_handler:
        handler = map_command_to_handler[command]
        handler(args)
    else:
        run_exe(command,args)

def handle_command(command : str, args: list[str])->None:
    executables = get_all_executable_commands()
    if command in SUPPORTED_COMMANDS:
        handler = map_command_to_handler[command]
        handler(args)
        return
    if command in executables:
        run_exe(command,args)
    else:
        print(f"invalid command : {command}")
    

USERNAME = os.getenv("USER")
HOSTNAME = socket.gethostname()

def main():
    while True:
        try :
            print(f"${USERNAME}@{HOSTNAME}$ ", end="")
            user_input = input().strip()
            command , args = parse_input(user_input)
            handle_command(command,args)
        except KeyboardInterrupt:
            print("Goodbye.")
            sys.exit(0)

         


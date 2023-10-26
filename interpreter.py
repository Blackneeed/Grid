import os
import sys
import colored
import colorama
import time

colorama.init(autoreset=1)

cprint = colored.cprint

try:
    file = sys.argv[1]
except IndexError:
    cprint(f"Syntax: {sys.argv[0]} <file>", "red")
    exit(-1)
if not os.path.exists(file):
    cprint(f"File '{file}' does not exist", "red")
    exit(-1)
with open(file, "r") as s:
    file_read = s.read()

j = 0

for l in file_read.splitlines():
    j+=1
    if l.lower().startswith("print"):
        if l.lower().startswith("print "):
            if l.removeprefix("print ").startswith("'") | l.endswith("'"):
                print(l.removeprefix("print '").removesuffix("'"))
        else:
            c = "print"
            cprint(f"[Err 1] SyntaxError unexpected string {l.removeprefix(c)} after 'print' at line {j} in file {file}", "red")
            exit(-1)
    if l.lower().startswith("cmd"):
        if l.lower().startswith("cmd "):
            os.system(l.removeprefix("cmd '").removesuffix("'"))
        else:
            c = "cmd"
            cprint(f"[Err 2] SyntaxError unexpected string {l.removeprefix(c)} after '{c}' at line {j} in file {file}", "red")
            exit(-1)
    if l.lower().startswith("run"):
        if l.lower().startswith("run "):
            os.startfile(l.removeprefix("run '").removesuffix("'"))
        else:
            c = "run"
            cprint(f"[Err 3] SyntaxError unexpected string {l.removeprefix(c)} after '{c}' at line {j} in file {file}", "red")
            exit(-1)
    if l.startswith("exit"):
        exit(0)
    if l.lower().startswith("wait"):
        if l.lower().startswith("wait "):
            time.sleep(int(l.removeprefix("wait ")))
        else:
            c = "wait"
            cprint(f"[Err 4] SyntaxError unexpected string {l.removeprefix(c)} after '{c}' at line {j} in file {file}", "red")
            exit(-1)
    if l.lower() == "pause":
        os.system("pause > nul")
import os
import shutil
import pathlib
import shlex

commands = ["chdir (chdir (path))", 'new (new (file / dir) "(file / dir name)")', 'del (del "(file / dir name)")', 'rdfile (rdfile "(file name)")', 'chfile (chfile "(file name)" (new file content))', 'move (move "(file name)" (path))', "walk (walk (path))", 'run (run "(filename)")', 'add (add "(filename)" (content))']

def script():
    path_dir = os.getcwd()

    print(path_dir)
    print("Type 'help' for help\n")

    for item in os.listdir(path_dir):
        full_path = os.path.join(path_dir, item)

        if os.path.isdir(full_path):
            print(f"[DIR] {item}")
        elif os.path.isfile(full_path):
            print(f"[FILE] {item}")

def reset():
    os.system("cls")
    script()

if __name__ == "__main__":
    os.chdir(pathlib.Path.home())
    reset()
    while True:
        cmd = shlex.split(input("> "))

        if not cmd:
            continue

        if cmd[0] in ["chdir", "del", "rdfile", "walk", "run"]:
            if len(cmd) < 2:
                print(f"{cmd[0]}: Missing argument")
                continue

        elif cmd[0] in ["new", "chfile", "move", "add"]:
            if len(cmd) < 3:
                print(f"{cmd[0]}: Missing argument")
                continue


        if cmd[0] == "chdir":
            try:
                os.chdir(" ".join(cmd[1:]))
            except (FileNotFoundError):
                print(f"chdir: Cannot find dir {' '.join(cmd[1:])}")
                continue

            except (OSError):
                print(f"chdir: Invalid argument {cmd[1]}")
                continue

        elif cmd[0] == "del":
            path_dir = os.getcwd()
            full_path = os.path.join(path_dir, cmd[1])

            if os.path.isfile(full_path):
                os.remove(full_path)
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path)

            else:
                print(f"del: Cannot {cmd[1]} not found")
                continue

        elif cmd[0] == "new":
            if cmd[1] == "file":
                if not os.path.exists(' '.join(cmd[2:])):
                    with open(' '.join(cmd[2:]), 'w') as f:
                        pass

                else:
                    print(f"new: File {' '.join(cmd[2:])} already exist")
                    continue

            elif cmd[1] == "dir":
                if not os.path.exists(' '.join(cmd[2:])):
                    os.mkdir(' '.join(cmd[2:]))
                else:
                    print(f"new: Folder {cmd[2]} already exist")

        elif cmd[0] == "chfile":
            try:
                if cmd[2] == "*":
                    with open(cmd[1], 'w') as f:
                        f.write("")
                elif cmd[2] != "*":
                    with open(cmd[1], 'w') as f:
                        f.write(" ".join(cmd[2:]))
            except (FileNotFoundError):
                print(f"chfile: File {cmd[1]} not found")
                continue

        elif cmd[0] == "rdfile":
            try:
                with open(' '.join(cmd[1:]), 'r') as f:
                    file = f.read()
                print(f"\n{file}")
                continue
            except (FileNotFoundError):
                print(f"rdfile: File {cmd[1]} not found")
                continue
            except:
                print(f"rdfile: Cannot read {' '.join(cmd[1:])}")
                continue

        elif cmd[0] == "move":
            try:
                shutil.move(cmd[1], cmd[2])
            except (FileNotFoundError):
                print(f"move: File {cmd[1]} or folder {cmd[2]} not found")
                continue

        elif cmd[0] == "walk":
            for root, dirs, files in os.walk(cmd[1], onerror=lambda e: print(f"dir: {e}")):
                print(f"Current: {root}")

                for dir_name in dirs:
                    print(f"[DIR] {dir_name}")
                for file_name in files:
                    print(f"[FILE] {file_name}")

            input("Press Enter to continue... ")

        elif cmd[0] == "run":
            try:
                os.startfile(cmd[1])
            except (FileNotFoundError):
                print(f"run: File {cmd[1]} not found")
                continue

        elif cmd[0] == "add":
            try:
                with open(cmd[1], 'a') as file:
                    file.write(" " + " ".join(cmd[2:]))

            except (FileNotFoundError):
                print(f"add: File {cmd[1]} not found")

        elif cmd[0] == "help":
            print("\ncommands:")

            for cmds in commands:
                print(cmds)

            continue

        else:
            print(f"Unknown command: {cmd[0]}")
            continue

        reset()

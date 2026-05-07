import os
import shutil

def script():
    path_dir = os.getcwd()

    for item in os.listdir(path_dir):
        full_path = os.path.join(path_dir, item)

        if os.path.isdir(full_path):
            print(f"[DIR] {item}")
        elif os.path.isfile(full_path):
            print(f"[FILE] {item}")

def reset():
    os.system("cls" if os.name == "nt" else "clear")
    script()

if __name__ == "__main__":
    reset()
    while True:
        cmd = input("> ").split()

        if not cmd:
            continue

        if cmd[0] == "chdir":
            if len(cmd) < 2:
                print("chdir: Missing argument")
                continue

            try:
                os.chdir(cmd[1])
            except (FileNotFoundError):
                print(f"chdir: Cannot find dir {cmd[1]}")
                continue

        elif cmd[0] == "del":
            if len(cmd) < 2:
                print("del: Missing argument")
                continue

            path_dir = os.getcwd()

            try:
                full_path = os.path.join(path_dir, cmd[1])

                if os.path.isfile(full_path):
                    os.remove(full_path)
                elif os.path.isdir(full_path):
                    shutil.rmtree(full_path)

            except (FileNotFoundError):
                print(f"del: Cannot find {cmd[1]}")

        elif cmd[0] == "new":
            if len(cmd) < 3:
                print("new: Missing argument")
                continue

            if cmd[1] == "file":
                if not os.path.exists(cmd[2]):
                    with open(cmd[2], 'w') as f:
                        if len(cmd) > 3:
                            f.write(" ".join(cmd[3:]))

                else:
                    print(f"new: File {cmd[2]} already exist")
                    continue

            elif cmd[1] == "dir":
                if not os.path.exists(cmd[2]):
                    os.mkdir(cmd[2])
                else:
                    print(f"new: Folder {cmd[2]} already exist")

        elif cmd[0] == "chfile":
            if len(cmd) < 3:
                print("chfile: Missing argument")
                continue

            try:
                with open(cmd[1], 'w') as f:
                    f.write(" ".join(cmd[2:]))
            except (FileNotFoundError):
                print(f"chfile: File {cmd[1]} not found")
                continue

        elif cmd[0] == "rdfile":
            if len(cmd) < 2:
                print("rdfile: Missing argument")
                continue

            try:
                with open(cmd[1], 'r') as f:
                    file = f.read()
                print(file)
                input("Press Enter to continue... ")
            except (FileNotFoundError):
                print(f"rdfile: File {cmd[1]} not found")
                continue
        
        elif cmd[0] == "move":
            if len(cmd) < 3:
                print("move: Missing argument")
                continue

            try:
                shutil.move(cmd[1], cmd[2])
            except (FileNotFoundError):
                print(f"move: File {cmd[1]} or folder {cmd[2]} not found")
                continue
        
        elif cmd[0] == "walk":
            if len(cmd) < 2:
                print("dir: Missing argument")
                continue

            for root, dirs, files in os.walk(cmd[1], onerror=lambda e: print(f"dir: {e}")):
                print(f"Current: {root}")

                for dir_name in dirs:
                    print(f"[DIR] {dir_name}")
                for file_name in files:
                    print(f"[FILE] {file_name}")
                
            input("Press Enter to continue... ")

        else:
            print(f"Unknown command: {cmd[0]}")
            continue

        reset()

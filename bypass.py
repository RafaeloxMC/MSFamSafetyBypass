import ctypes, subprocess, sys, os
print(""" /$$      /$$  /$$$$$$        /$$$$$$$$                      /$$$$$$             /$$$$$$            /$$              
| $$$    /$$$ /$$__  $$      | $$_____/                     /$$__  $$           /$$__  $$          | $$              
| $$$$  /$$$$| $$  \__/      | $$    /$$$$$$  /$$$$$$/$$$$ | $$  \__/  /$$$$$$ | $$  \__//$$$$$$  /$$$$$$   /$$   /$$
| $$ $$/$$ $$|  $$$$$$       | $$$$$|____  $$| $$_  $$_  $$|  $$$$$$  |____  $$| $$$$   /$$__  $$|_  $$_/  | $$  | $$
| $$  $$$| $$ \____  $$      | $$__/ /$$$$$$$| $$ \ $$ \ $$ \____  $$  /$$$$$$$| $$_/  | $$$$$$$$  | $$    | $$  | $$
| $$\  $ | $$ /$$  \ $$      | $$   /$$__  $$| $$ | $$ | $$ /$$  \ $$ /$$__  $$| $$    | $$_____/  | $$ /$$| $$  | $$
| $$ \/  | $$|  $$$$$$/      | $$  |  $$$$$$$| $$ | $$ | $$|  $$$$$$/|  $$$$$$$| $$    |  $$$$$$$  |  $$$$/|  $$$$$$$
|__/     |__/ \______/       |__/   \_______/|__/ |__/ |__/ \______/  \_______/|__/     \_______/   \___/   \____  $$
                                                                                                            /$$  | $$
                                                                                                           |  $$$$$$/
                                                                                                            \______/ """)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if not is_admin():
    subprocess.call("cls", shell=True)
    print("Admin privileges required, please run as admin...")
    hinstance = ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, sys.argv[0], None, 1)
    sys.exit()

print("Working...")
while True:
    subprocess.DEVNULL = open(os.devnull, 'w')
    subprocess.call("taskkill -f -im WpcMon.exe", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
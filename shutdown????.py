import os
import sys


def shutdown_laptop():
    # Detect the operating system
    os_type = sys.platform

    if os_type.startswith("win32"):
        # Windows: /s triggers shutdown, /t 0 sets the countdown timer to 0 seconds
        os.system("shutdown /s /t 0")

    elif os_type.startswith("linux"):
        # Linux: 'now' executes it immediately (may require sudo privileges)
        os.system("shutdown now")

    elif os_type.startswith("darwin"):
        # macOS: Executes immediate shutdown (requires root/sudo privileges)
        os.system("sudo shutdown -h now")

    else:
        print("Operating system not supported.")


# shutdown_laptop()
# remove # in above line

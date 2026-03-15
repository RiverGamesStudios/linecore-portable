#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of LineCoreOS in Python."""

# pylint: disable=global-statement
import zipfile
import io
import os
import time
import random
import sys
import hashlib
import scratch3
import applets
import LineRenderer
import linative

LINECORE_VERSION = "0.0.57"
LINESHELL_VERSION = "0.0.5713"
LINECORE_SETUP_UTILITY_VERSION = "0.7.70516"

argv: list = sys.argv
argv.pop(0)

linecore_portable = False
native = False

for arg in argv:
    if arg in ("--portable", "-p"):
        linecore_portable = True
    if arg in ("--native", "-n"):
        native = True
    if arg in ("--list-applets", "-a"):
        print("Supported applets:")
        for applet in applets.__all__:
            print(applet[7:])
        sys.exit(0)
    if arg in ("-h", "/?", "--help"):
        print(f"LineCore Portable {LINECORE_VERSION}-portable")
        print("Arguments:")
        print("\t --portable, -p: Custom LineCore Portable changes to LineCoreOS")
        print("\t --native, -n: Power-related commands are also synced to host.")
        print("\t --list-applets, -a: Show all supported applets")
        print("\t -h, /?, --help: Show this help message")
        print()
        print("LineCore Portable is made by NexusSfan")
        print("LineCoreOS is made by Cole Bohte")
        sys.exit(0)

DeviceName = scratch3.Variable("SYSTEM")
ConsoleInput = scratch3.Variable("")
SystemSoftwareVer = scratch3.Variable(
    LINECORE_VERSION + ("-portable" if linecore_portable else "")
)
ShellVer = scratch3.Variable(
    LINESHELL_VERSION + ("-portable" if linecore_portable else "")
)
SetupUtilityVer = scratch3.Variable(
    LINECORE_SETUP_UTILITY_VERSION + ("-portable" if linecore_portable else "")
)
CurrentFSLocation = scratch3.Variable("")
CurrentUser = scratch3.Variable("")
CurrentApp = scratch3.Variable("")
OnShell = scratch3.Variable(False)
RegisteredUsers = scratch3.List()
LFS = None  # NOTE: This variable `LFS` is more like the "current mount" object instead of the LFS mount object
mounts = {"LFS": LFS}
pwd = ""
current_mount = "LFS"
current_cmd = scratch3.Variable("")

# Add stuff to terminalrenderagent without running the functions!
# super(type(LineRenderer.TerminalRenderAgent), LineRenderer.TerminalRenderAgent).add("stuff")


def create_dir_lfsinit(path: str) -> None:
    LineRenderer.TerminalRenderAgent.add(
        f'LFSINIT: Creating Directory "{path}" on drive "LFS"'
    )
    LFS.writestr(f"{path}/", b"")


def init() -> None:
    LineRenderer.InputLine.change("default | INIT @ SYSTEM :")
    time.sleep(1)
    LineRenderer.TerminalRenderAgent.add("Initializing TerminalRenderAgent.tm")
    time.sleep(random.randint(5, 30) / 10)
    LineRenderer.TerminalRenderAgent.add("TerminalRenderAgent.tm Finished")
    time.sleep(0.1)
    LineRenderer.TerminalRenderAgent.add("Loading LFSINIT")
    time.sleep(random.randint(1, 20) / 10)
    LineRenderer.TerminalRenderAgent.add("LFSINIT: Initializing LFS")
    time.sleep(0.5)
    global LFS
    LFS = zipfile.ZipFile(io.BytesIO(), "w")
    mounts["LFS"] = LFS
    LineRenderer.TerminalRenderAgent.add('LFSINIT: Switching to drive "LFS"')
    create_dir_lfsinit("user")
    create_dir_lfsinit("opt")
    create_dir_lfsinit("fsdata")
    # this is never used
    if not linecore_portable:
        LineRenderer.TerminalRenderAgent.add(
            'LFSINIT: Creating Directory "setup" on drive "LFS"'
        )
    create_dir_lfsinit("user/setupuser")
    create_dir_lfsinit("user/setupuser/Documents")
    create_dir_lfsinit("user/setupuser/Applets")
    create_dir_lfsinit("opt/userdata")
    create_dir_lfsinit("opt/systemdata")
    # this folder is created in LineCoreOS but not mentioned in LFSINIT
    if linecore_portable:
        LineRenderer.TerminalRenderAgent.add(
            'LFSINIT: Creating Directory "opt/userdata/setupuser" on drive "LFS"'
        )
    LFS.writestr("opt/userdata/setupuser/", b"")
    LineRenderer.TerminalRenderAgent.add("LFSINIT: Cleaning up file system...")
    time.sleep(0.125)
    LineRenderer.TerminalRenderAgent.add("LFSINIT: Finished")
    time.sleep(0.125)
    LineRenderer.TerminalRenderAgent.add("Creating auto-generated System Settings")
    LFS.writestr("opt/userdata/setupuser/bgcolour.pref", "#000000")
    LFS.writestr("opt/userdata/setupuser/textcolour.pref", "#FFFFFF")
    LFS.writestr("opt/userdata/setupuser/textcursor.pref", "_")
    LFS.writestr("opt/userdata/setupuser/presshold.pref", "0.3")
    LFS.writestr("opt/systemdata/devicename.pref", "SYSTEM")
    LFS.writestr("opt/systemdata/defaultpromptlocation.pref", "/user/setupuser/")
    LFS.writestr("opt/systemdata/region.pref", "International")
    LFS.writestr(
        "opt/userdata/setupuser/user.pwrd",
        hashlib.sha256("password".encode()).hexdigest(),
    )
    LFS.writestr("opt/userdata/setupuser/pwrdenabled.pref", "false")
    time.sleep(1)
    LineRenderer.TerminalRenderAgent.add("Creating auto-generated User Settings")
    time.sleep(1)


def initialize_user(username: str) -> None:
    LineRenderer.TerminalRenderAgent.add("Loading User Preferences...")
    time.sleep(1)
    OnShell.change(True)
    CurrentApp.change("")
    CurrentUser.change(username)


def initFinished() -> None:
    global LFS
    OnShell.change(True)
    LineRenderer.TerminalRenderAgent.clear()
    LineRenderer.TerminalRenderAgent.add(
        f"Welcome to LineCoreOS v{SystemSoftwareVer.get()}"
    )
    LineRenderer.TerminalRenderAgent.add("Loading System Preferences...")
    time.sleep(1)
    if os.path.exists("LFS.zip"):
        LFS.close()
        with zipfile.ZipFile("LFS.zip", "r") as lfs_zip_object:
            LFS = zipfile.ZipFile(io.BytesIO(), "w")
            mounts["LFS"] = LFS
            for file_info in lfs_zip_object.infolist():
                data = lfs_zip_object.read(file_info.filename)
                LFS.writestr(file_info, data)
    userdir = zipfile.Path(LFS, "user/")
    users_dirs = [i.name for i in userdir.iterdir()]
    time.sleep(2)
    OnShell.change(False)
    CurrentApp.change("login")
    CurrentFSLocation.change("LOGIN")
    LineRenderer.InputLine.change(f"default | LOGIN @ {DeviceName.get()} :")
    LineRenderer.TerminalRenderAgent.add("")
    LineRenderer.TerminalRenderAgent.add("For default user: Use 'setupuser'")
    LineRenderer.TerminalRenderAgent.add("")
    LineRenderer.TerminalRenderAgent.add("LineCoreOS User:")
    tempUser = input("")
    # todo: fix compat with linecoreos
    LineRenderer.TerminalRenderAgent.add(
        f"default | LOGIN @ {DeviceName.get()} : {tempUser}"
    )
    while tempUser not in users_dirs:
        LineRenderer.TerminalRenderAgent.add("User does not exist; please try again.")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("LineCoreOS User:")
        tempUser = input("")
        LineRenderer.TerminalRenderAgent.add(
            f"default | LOGIN @ {DeviceName.get()} : {tempUser}"
        )
    with LFS.open(f"opt/userdata/{tempUser}/pwrdenabled.pref", "r") as f:
        if f.read() == b"true":
            OnShell.change(False)
            CurrentApp.change("pwrd")
            CurrentFSLocation.change("PWRD")
            LineRenderer.TerminalRenderAgent.add("Please wait...")
            time.sleep(1)
            LineRenderer.TerminalRenderAgent.add("")
            LineRenderer.TerminalRenderAgent.add("Password:")
            tempPassword = input()
            with LFS.open(f"opt/userdata/{tempUser}/user.pwrd") as passf:
                while (
                    hashlib.sha256(tempPassword.encode()).hexdigest().encode()
                    != passf.read()
                ):
                    LineRenderer.TerminalRenderAgent.add("")
                    LineRenderer.TerminalRenderAgent.add("Password:")
                    tempPassword = input()
            initialize_user(tempUser)
        # elif f.read() == b'false':
        # ^ That is not how the compat works
        else:
            initialize_user(tempUser)


def sync_color() -> None:
    currentuser = CurrentUser.get()
    global LFS
    with LFS.open(f"opt/userdata/{currentuser}/textcolour.pref") as f1:
        LineRenderer.TextColor.change(f1.read().decode())
    with LFS.open(f"opt/userdata/{currentuser}/bgcolour.pref") as f2:
        LineRenderer.BgColor.change(f2.read().decode())


def sync_pwd() -> None:
    CurrentFSLocation.change(f"{current_mount}/{pwd}")


def startShell() -> None:
    LineRenderer.TerminalRenderAgent.clear()
    LineRenderer.TerminalRenderAgent.add(
        f"LineShell v{ShellVer.get()} on LineCoreOS v{SystemSoftwareVer.get()}"
    )
    LineRenderer.TerminalRenderAgent.add(
        "Type 'help' for information on using LineShell"
    )
    LineRenderer.TerminalRenderAgent.add("Run 'setup' to configure LineCoreOS settings")
    global pwd
    pwd = f"user/{CurrentUser.get()}/"


def sync_ps1() -> None:
    LineRenderer.InputLine.change(
        f"{CurrentUser.get()} | {CurrentFSLocation.get()} @ {DeviceName.get()} :"
    )


def sync_shellinfo() -> None:
    sync_pwd()
    sync_ps1()
    sync_color()
    LineRenderer.Function()


def shell_input() -> None:
    console_command = input()
    current_cmd.change(console_command)
    LineRenderer.TerminalRenderAgent.add(
        f"{LineRenderer.InputLine.get()} {console_command}"
    )
    if OnShell.get():
        if console_command == "clear":
            LineRenderer.TerminalRenderAgent.clear()
        elif console_command == "fetch":
            applets.applet_fetch(globals())
        elif console_command == "help":
            applets.applet_help(globals())
        elif console_command == "off":
            applets.applet_off(globals())
        elif console_command == "lineshell":
            applets.applet_lineshell(globals())
        elif console_command.startswith("cd"):
            applets.applet_cd(globals())
        elif console_command == "ls":
            applets.applet_ls(globals())
        elif console_command == "time":
            applets.applet_time(globals())
        elif console_command == "date":
            applets.applet_date(globals())
        elif console_command == "shutdown":
            applets.applet_shutdown(globals())
        elif console_command == "reboot":
            applets.applet_reboot(globals())
        elif console_command == "setup":
            applets.applet_setup(globals())
        elif console_command.startswith("read"):
            applets.applet_read(globals())
        elif console_command.startswith("md"):
            applets.applet_md(globals())
        elif console_command.startswith("rd"):
            applets.applet_rd(globals())
        elif console_command.startswith("dl"):
            applets.applet_dl(globals())
        elif console_command.startswith("am"):
            applets.applet_am(globals())
        elif console_command.startswith("sm"):
            applets.applet_sm(globals())
        elif console_command.startswith("rm"):
            applets.applet_rm(globals())
        elif console_command.startswith("lm"):
            applets.applet_lm(globals())
        elif console_command.startswith("write"):
            applets.applet_write(globals())
        OnShell.change(1)
        CurrentApp.change("")

def Function() -> None:
    init()
    initFinished()
    sync_color()
    startShell()

    while True:
        try:
            sync_shellinfo()
            shell_input()
        except KeyboardInterrupt: # todo: fix compat
            LineRenderer.TerminalRenderAgent.add(LineRenderer.InputLine.get())


if __name__ == "__main__":
    Function()

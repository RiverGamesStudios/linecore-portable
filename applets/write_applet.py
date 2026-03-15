# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the write applet from LineCore OS in Python."""
import sys
import termios
import tty
import os
import applets.libapplet

def get_char():
    """Gets character from stdin."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def get_key_pressed() -> str:
    """Gets key pressed from stdin."""
    char = get_char()
    if char == "\x03":
        return "^C"
    if char == "\x18":
        return "^X"
    if char == "\x13":
        return "^S"
    if char == "\x7f":
        return "^BKSP"
    return char

def applet_write(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    CurrentFSLocation = globals_list["CurrentFSLocation"]
    CurrentUser = globals_list["CurrentUser"]
    DeviceName = globals_list["DeviceName"]
    LFS = globals_list["LFS"]
    pwd = globals_list["pwd"]
    linecore_portable = globals_list["linecore_portable"]
    filename = ""
    current_cmd: str = globals_list["current_cmd"].get()
    if current_cmd == "write #help":
        LineRenderer.TerminalRenderAgent.add("WRITE Help")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("WRITE is an extremely simple, lightweight text editor built for LineCoreOS")
        LineRenderer.TerminalRenderAgent.add("WRITE supports all text file types.")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("Example Usage:")
        LineRenderer.TerminalRenderAgent.add("'write notes.txt'")
        return
    if current_cmd == "write" and linecore_portable:
        return
    filename = current_cmd.replace("write ", "")
    globals_list["OnShell"].change(0)
    globals_list["CurrentApp"].change("write")
    CurrentFSLocation.change("WRITE")
    applets.libapplet.update_ps1(globals_list)
    combinedpath = os.path.join(pwd, filename)
    checkparser = applets.libapplet.does_file_exist(LFS, combinedpath)
    KbdInput = []
    if checkparser:
        fileread = LFS.read(combinedpath).decode()
        KbdInput = list(fileread)
    LineRenderer.EmptyLineEnabled.change(False)
    notif = ""
    while True:
        LineRenderer.TerminalRenderAgent.clear()
        LineRenderer.TerminalRenderAgent.add(f"LineCoreOS Write - {filename}")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add(f"{CurrentUser.get()} | {CurrentFSLocation.get()} @ {DeviceName.get()} : {''.join(KbdInput)}")
        for _ in range(23):
            LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add(f"{notif}")
        LineRenderer.TerminalRenderAgent.add("^S - Save     ^X - Save & Quit     ^C - Force Quit")
        LineRenderer.Function()
        char_latest_input = get_key_pressed()
        if char_latest_input == "^BKSP":
            if KbdInput:
                KbdInput.pop(-1)
        elif char_latest_input == "^C":
            LineRenderer.EmptyLineEnabled.change(True)
            LineRenderer.TerminalRenderAgent.clear()
            return
        elif char_latest_input == "^X":
            LFS.writestr(combinedpath, ''.join(KbdInput))
            LineRenderer.EmptyLineEnabled.change(True)
            LineRenderer.TerminalRenderAgent.clear()
            LineRenderer.TerminalRenderAgent.add(f"WRITE: '{filename}' saved successfully.")
            return
        elif char_latest_input == "^S":
            LFS.writestr(combinedpath, ''.join(KbdInput))
            # todo: fix compat, this should not stay forever
            notif = f"'{filename}' saved successfully."
        else:
            KbdInput.append(char_latest_input)

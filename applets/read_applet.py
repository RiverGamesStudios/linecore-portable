# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the read applet from LineCore OS in Python."""
import os
import applets.libapplet

def applet_read(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    current_cmd = globals_list["current_cmd"].get()
    linecore_portable = globals_list["linecore_portable"]
    LFS = globals_list["LFS"]
    pwd = globals_list["pwd"]
    if current_cmd == "read #help":
        LineRenderer.TerminalRenderAgent.add("READ Help")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("READ works by displaying the contents of the user specified file.")
        LineRenderer.TerminalRenderAgent.add("READ supports all text file types.")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("Example Usage:")
        LineRenderer.TerminalRenderAgent.add("'read notes.txt'")
        return
    # bug: if you just type `read` it will read the file called "read"
    # this is to keep compat with LineCore
    if linecore_portable:
        if current_cmd == "read":
            return
    arg = current_cmd.replace("read ", "")
    combinedpath = os.path.join(pwd, arg)
    LineRenderer.TerminalRenderAgent.add(f"Contents of file '{arg}':")
    fileread = ""
    checkparser = applets.libapplet.does_file_exist(LFS, combinedpath)
    if checkparser:
        fileread = LFS.read(combinedpath).decode()
    LineRenderer.TerminalRenderAgent.add(f"{fileread}")

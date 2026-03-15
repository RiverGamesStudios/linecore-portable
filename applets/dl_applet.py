# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the dl applet from LineCore OS in Python."""
import os
import applets.libapplet

def applet_dl(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    LFS = globals_list["LFS"]
    pwd = globals_list["pwd"]
    linecore_portable = globals_list["linecore_portable"]
    current_cmd = globals_list["current_cmd"].get()
    if current_cmd == "dl #help":
        LineRenderer.TerminalRenderAgent.add("DL Help")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("DL works by deleting the user specified file.")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("Example Usage:")
        LineRenderer.TerminalRenderAgent.add("'dl math.txt'")
        return
    if current_cmd == "dl" and linecore_portable:
        return
    arg = current_cmd.replace("dl ", "")
    if arg == "":
        LineRenderer.TerminalRenderAgent.add(f"DL: Error when deleting file '{arg}'; please specify a file name.")
        return
    combinedpath = os.path.join(pwd, arg)
    globals_list["LFS"] = applets.libapplet.delete_file(LFS, combinedpath)
    if linecore_portable:
        LineRenderer.TerminalRenderAgent.add(f"DL: Deleted file '{arg}' successfully")

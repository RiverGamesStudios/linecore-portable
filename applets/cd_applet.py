# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the cd applet from LineCore OS in Python."""
import os
import zipfile

def applet_cd(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    LFS = globals_list["LFS"]
    pwd = globals_list["pwd"]
    linecore_portable = globals_list["linecore_portable"]
    current_cmd = globals_list["current_cmd"].get()
    if current_cmd == "cd #help":
        LineRenderer.TerminalRenderAgent.add("CD Help")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("CD works on adding the given path to the current directory.")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("Example Usage:")
        LineRenderer.TerminalRenderAgent.add("'cd ../setupuser'")
        return
    if current_cmd == "cd":
        return
    arg = current_cmd.replace("cd ", "")
    combinedpath = os.path.join(pwd, arg)
    if combinedpath.endswith("/") and not linecore_portable:
        return
    parsedpath = os.path.normpath(combinedpath)
    if parsedpath != '.':
        parsedpathwithslash = f"{parsedpath}/"
    else:
        parsedpathwithslash = ""
    checkparser = zipfile.Path(LFS, parsedpathwithslash)
    if parsedpathwithslash == "" or checkparser.exists():
        globals_list["pwd"] = parsedpathwithslash

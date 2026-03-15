# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the md applet from LineCore OS in Python."""
import os
import zipfile

def applet_md(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    LFS = globals_list["LFS"]
    pwd = globals_list["pwd"]
    linecore_portable = globals_list["linecore_portable"]
    current_cmd = globals_list["current_cmd"].get()
    if current_cmd == "md #help":
        LineRenderer.TerminalRenderAgent.add("MD Help")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("MD works by creating a directory with the user specified name.")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("Example Usage:")
        LineRenderer.TerminalRenderAgent.add("'md Homework'")
        return
    if current_cmd == "md" and linecore_portable:
        return
    arg = current_cmd.replace("md ", "")
    if "/" in arg:
        LineRenderer.TerminalRenderAgent.add(f"MD: Error when creating directory '{arg}/'; directory name cannot contain '/'.")
        return
    combinedpath = os.path.join(pwd, arg)
    slashpath = f"{combinedpath}/"
    checkparser = zipfile.Path(LFS, slashpath)
    LineRenderer.TerminalRenderAgent.add(f"MD: Created directory '{arg}/' successfully")
    if not checkparser.exists():
        LFS.writestr(slashpath, b"")

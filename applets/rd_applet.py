# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the rd applet from LineCore OS in Python."""
import os
import applets.libapplet

def applet_rd(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    LFS = globals_list["LFS"]
    pwd = globals_list["pwd"]
    linecore_portable = globals_list["linecore_portable"]
    current_cmd = globals_list["current_cmd"].get()
    if current_cmd == "rd #help":
        LineRenderer.TerminalRenderAgent.add("RD Help")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("RD works by removing the user specified directory.")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("Example Usage:")
        LineRenderer.TerminalRenderAgent.add("'rd Homework'")
        return
    if current_cmd == "rd" and linecore_portable:
        return
    arg = current_cmd.replace("rd ", "")
    if arg == "":
        LineRenderer.TerminalRenderAgent.add(f"RD: Error when deleting directory '{arg}/'; please specify a directory name.")
        return
    combinedpath = os.path.join(pwd, arg)
    slashpath = f"{combinedpath}/"
    globals_list["LFS"] = applets.libapplet.delete_dir(LFS, slashpath)
    LineRenderer.TerminalRenderAgent.add(f"RD: Removed directory '{arg}/' successfully")

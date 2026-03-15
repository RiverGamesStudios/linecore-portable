# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the sm applet from LineCore OS in Python."""

def applet_sm(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    mounts = globals_list["mounts"]
    linecore_portable = globals_list["linecore_portable"]
    current_cmd = globals_list["current_cmd"].get()
    if current_cmd == "sm #help":
        LineRenderer.TerminalRenderAgent.add("SM Help")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("SM works by switching to the user specified mount.")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("Example Usage:")
        LineRenderer.TerminalRenderAgent.add("'sm ExternalStorage'")
        return
    if current_cmd == "sm" and linecore_portable:
        return
    arg = current_cmd.replace("sm ", "")
    if arg == "":
        globals_list["LFS"] = mounts["LFS"]
        return
    globals_list["pwd"] = ""
    globals_list["LFS"] = mounts[arg]
    globals_list["current_mount"] = arg

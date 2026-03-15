# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the rm applet from LineCore OS in Python."""

def applet_rm(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    linecore_portable = globals_list["linecore_portable"]
    current_cmd = globals_list["current_cmd"].get()
    mounts = globals_list["mounts"]
    if current_cmd == "rm #help":
        LineRenderer.TerminalRenderAgent.add("rm Help")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("RM works by removing the user specified mount.")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("Example Usage:")
        LineRenderer.TerminalRenderAgent.add("'rm ExternalStorage'")
        return
    if current_cmd == "rm" and linecore_portable:
        return
    arg = current_cmd.replace("rm ", "")
    if arg == "" and linecore_portable:
        return
    if arg == "LFS":
        LineRenderer.TerminalRenderAgent.add("RM: Failed to remove mount; the system mount cannot be removed")
        return
    globals_list["mounts"].pop(arg, None)
    globals_list["LFS"] = mounts["LFS"]
    globals_list["current_mount"] = "LFS"

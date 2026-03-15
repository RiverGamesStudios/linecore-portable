# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the help applet from LineCore OS in Python."""

def applet_help(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    LineRenderer.TerminalRenderAgent.add("LineShell Help")
    LineRenderer.TerminalRenderAgent.add("")
    LineRenderer.TerminalRenderAgent.add("LineShell Commands:")
    LineRenderer.TerminalRenderAgent.add("help - Displays a list of commands")
    LineRenderer.TerminalRenderAgent.add("clear - Clears the screen")
    LineRenderer.TerminalRenderAgent.add("reboot - Reboots the system")
    LineRenderer.TerminalRenderAgent.add("shutdown - Shuts the system down")
    LineRenderer.TerminalRenderAgent.add("ls - Lists the current directory")
    LineRenderer.TerminalRenderAgent.add("cd - Change directory")
    LineRenderer.TerminalRenderAgent.add("time - View current time & timezone")
    LineRenderer.TerminalRenderAgent.add("date - View current date")
    LineRenderer.TerminalRenderAgent.add("md - Creates a new directory")
    LineRenderer.TerminalRenderAgent.add("rd - Removes a directory")
    LineRenderer.TerminalRenderAgent.add("dl - Deletes a file")
    LineRenderer.TerminalRenderAgent.add("sm - Sets the current drive mount")
    LineRenderer.TerminalRenderAgent.add("am - Adds drive mount via HTTPS")
    LineRenderer.TerminalRenderAgent.add("rm - Removes drive mount")
    LineRenderer.TerminalRenderAgent.add("lm - Lists all drive mounts")
    LineRenderer.TerminalRenderAgent.add("")
    LineRenderer.TerminalRenderAgent.add("Programs:")
    LineRenderer.TerminalRenderAgent.add("setup - The LineCoreOS Setup Utility")
    LineRenderer.TerminalRenderAgent.add("lineshell - The shell designed for LineCoreOS & LineFS")
    LineRenderer.TerminalRenderAgent.add("fetch - A simple fetch program")
    LineRenderer.TerminalRenderAgent.add("read - A barebones text file viewer")
    LineRenderer.TerminalRenderAgent.add("write - An ultra-simple, lightweight text editor for LineCoreOS")

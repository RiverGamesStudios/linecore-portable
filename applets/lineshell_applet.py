# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the lineshell applet from LineCore OS in Python."""

def applet_lineshell(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    LineRenderer.TerminalRenderAgent.add("LINESHELL: Failed to start LineShell.")
    LineRenderer.TerminalRenderAgent.add("LINESHELL: Another LineShell instance is already running.")

# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the lm applet from LineCore OS in Python."""

def applet_lm(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    LineRenderer.TerminalRenderAgent.add("Showing all mounts:")
    mounts = ' '.join(globals_list["mounts"].keys())
    LineRenderer.TerminalRenderAgent.add(mounts)

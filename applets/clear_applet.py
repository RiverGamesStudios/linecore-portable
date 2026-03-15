# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the clear applet from LineCore OS in Python."""

def applet_clear(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    LineRenderer.TerminalRenderAgent.clear()

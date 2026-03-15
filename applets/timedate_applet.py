# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the time/date applet from LineCore OS in Python."""
from datetime import datetime, timezone

def applet_time(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    current_time = datetime.now().strftime('%H:%M:%S')
    LineRenderer.TerminalRenderAgent.add(f"{current_time}")

    # todo: fix compat with utc timezone detection
    now = datetime.now(timezone.utc)
    utc_offset = now.utcoffset()
    offset_hours = int(utc_offset.total_seconds() / 3600)
    offset_str = f"UTC{'+' if offset_hours >= 0 else '-'}{abs(offset_hours):02d}"
    LineRenderer.TerminalRenderAgent.add(f"{offset_str}")

def applet_date(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    current_date = datetime.today().strftime('%Y-%m-%d')
    LineRenderer.TerminalRenderAgent.add(f"{current_date}")

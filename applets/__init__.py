# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the applets from LineCore OS in Python."""

from .help_applet import applet_help
from .fetch_applet import applet_fetch
from .off_applet import applet_off, applet_shutdown, applet_reboot
from .lineshell_applet import applet_lineshell
from .cd_applet import applet_cd
from .ls_applet import applet_ls
from .timedate_applet import applet_time, applet_date
from .read_applet import applet_read
from .md_applet import applet_md
from .rd_applet import applet_rd
from .dl_applet import applet_dl
from .am_applet import applet_am
from .sm_applet import applet_sm
from .rm_applet import applet_rm
from .lm_applet import applet_lm
from .setup_applet import applet_setup
from .write_applet import applet_write

__all__ = [
    "applet_help",
    "applet_fetch",
    "applet_off",
    "applet_lineshell",
    "applet_cd",
    "applet_ls",
    "applet_time",
    "applet_date",
    "applet_read",
    "applet_md",
    "applet_rd",
    "applet_dl",
    "applet_shutdown",
    "applet_am",
    "applet_sm",
    "applet_rm",
    "applet_lm",
    "applet_reboot",
    "applet_setup",
    "applet_write",
]

# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Features used in Native LineCore Portable."""
import sys
import os


def shutdown() -> None:
    if sys.platform == "win32":
        os.system("shutdown /s /t 0")
        return
    raise OSError("Unable to reboot")


def reboot() -> None:
    if sys.platform == "win32":
        os.system("shutdown /r /t 0")
        return
    raise OSError("Unable to reboot")

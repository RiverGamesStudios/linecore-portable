# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the fetch applet from LineCore OS in Python."""
import os
import time
import pyautogui

def applet_fetch(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    SystemSoftwareVer = globals_list["SystemSoftwareVer"].get()
    ShellVer = globals_list["ShellVer"].get()
    LFS = globals_list["LFS"]
    current_mount = globals_list["current_mount"]
    screen_res = pyautogui.size()
    screen_width = screen_res.width
    screen_height = screen_res.height
    LineRenderer.TerminalRenderAgent.add(LineRenderer.InputLine.get())
    LineRenderer.TerminalRenderAgent.add("")
    LineRenderer.TerminalRenderAgent.add(f"   @@@@@               @@@@@@@@@@@@@@@       OS: LineCoreOS v{SystemSoftwareVer}")
    with LFS.open("opt/systemdata/devicename.pref") as f:
        LineRenderer.TerminalRenderAgent.add(f"   @@@@@             @@@@@@@@@@@@@@@@@@@     Host: {f.read().decode()}")
    LineRenderer.TerminalRenderAgent.add(f"   @@@@@           @@@@@@           @@@@@@   Kernel: LineKernel{SystemSoftwareVer}")
    LineRenderer.TerminalRenderAgent.add(f"   @@@@@           @@@@@                     Uptime: {round(time.monotonic())}")
    LineRenderer.TerminalRenderAgent.add("   @@@@@           @@@@@                     Installed Packages: 5 (LineCoreOS)")
    LineRenderer.TerminalRenderAgent.add(f"   @@@@@           @@@@@@           @@@@@@   Shell: LineShell v{ShellVer}")
    LineRenderer.TerminalRenderAgent.add(f"   @@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@     Display Resolution: {screen_width}x{screen_height}")
    LineRenderer.TerminalRenderAgent.add(f"   @@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@       Render Resolution: {screen_width}x{screen_height}") # terminal doesn't have render res i guess
    LineRenderer.TerminalRenderAgent.add(f"                                             Scaled Resolution: {screen_width}x{screen_height}") # terminal doesn't have scaled res i guess
    LineRenderer.TerminalRenderAgent.add("        @@@@@@@@@@@@@            @@@@@@@     Terminal: LineCoreOS TTY")
    LineRenderer.TerminalRenderAgent.add(f"     @@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@  CPU Threads: {os.cpu_count()}")
    LineRenderer.TerminalRenderAgent.add("   @@@@@@@         @@@@@@   @@@@@      @@@@@ GPU: Unknown") # todo: implement
    LineRenderer.TerminalRenderAgent.add(f"   @@@@@            @@@@@@  @@@@@@@@@@       Current Disk: {current_mount}")
    LineRenderer.TerminalRenderAgent.add("  @@@@@             @@@@@@    @@@@@@@@@@@@   ╔═══════╗")
    LineRenderer.TerminalRenderAgent.add("   @@@@@           @@@@@@           @@@@@@   ║ ██|   ║")
    LineRenderer.TerminalRenderAgent.add("   @@@@@@@@    @@@@@@@@@  @@@@@@    @@@@@@   ╚═══════╝")
    LineRenderer.TerminalRenderAgent.add("     @@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@    ")
    LineRenderer.TerminalRenderAgent.add("         @@@@@@@@             @@@@@@@@       ")
    LineRenderer.TerminalRenderAgent.add("")

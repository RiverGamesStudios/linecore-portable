# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the off applet from LineCore OS in Python."""
import sys
import time
import datetime
import zipfile

def applet_off(globals_list: list) -> None:
    if globals_list["native"]:
        globals_list["linative"].shutdown()
    else:
        sys.exit(0)

def applet_shutdown(globals_list: list) -> None:
    OnShell = globals_list["OnShell"]
    OnShell.change(False)
    CurrentApp = globals_list["CurrentApp"]
    CurrentApp.change("shutdown")
    CurrentFSLocation = globals_list["CurrentFSLocation"]
    CurrentFSLocation.change("SHUTDOWN")
    CurrentUser = globals_list["CurrentUser"]
    LineRenderer = globals_list["LineRenderer"]
    DeviceName = globals_list["DeviceName"]
    real_LFS = globals_list["mounts"]["LFS"]
    mounts = globals_list["mounts"]
    LineRenderer.InputLine.change(
        f"{CurrentUser.get()} | {CurrentFSLocation.get()} @ {DeviceName.get()} :"
    )
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    LineRenderer.TerminalRenderAgent.add(f"Shutdown called @ {formatted_time} for system '{DeviceName.get()}'")
    LineRenderer.TerminalRenderAgent.add("Rebooting in 5")
    time.sleep(1)
    LineRenderer.TerminalRenderAgent.remove(len(list(LineRenderer.TerminalRenderAgent)))
    LineRenderer.TerminalRenderAgent.add("Rebooting in 4")
    time.sleep(1)
    LineRenderer.TerminalRenderAgent.remove(len(list(LineRenderer.TerminalRenderAgent)))
    LineRenderer.TerminalRenderAgent.add("Rebooting in 3")
    time.sleep(1)
    LineRenderer.TerminalRenderAgent.remove(len(list(LineRenderer.TerminalRenderAgent)))
    LineRenderer.TerminalRenderAgent.add("Rebooting in 2")
    time.sleep(1)
    LineRenderer.TerminalRenderAgent.remove(len(list(LineRenderer.TerminalRenderAgent)))
    LineRenderer.TerminalRenderAgent.add("Rebooting in 1")
    time.sleep(1)
    LineRenderer.TerminalRenderAgent.remove(len(list(LineRenderer.TerminalRenderAgent)))
    LineRenderer.TerminalRenderAgent.add("Rebooting...")
    time.sleep(1)
    LineRenderer.TerminalRenderAgent.clear()
    # yes, this is really the way to export to a ZIP on the disk in zipfile. horrible design.
    with zipfile.ZipFile('LFS.zip', 'w') as zip_write:
        for file_info in real_LFS.infolist():
            # SHORE said that this is supposed to save all mounts but that doesn't make sense
            # it only loads LFS.zip from storage, nothing else.
            # Also see: [Sprite applets//setup]
            data = real_LFS.read(file_info.filename)
            zip_write.writestr(file_info, data)
    for _, value in mounts.items():
        value.close()
    LineRenderer.TerminalRenderAgent.add("It is now safe to power off.")
    LineRenderer.TerminalRenderAgent.add("")
    LineRenderer.TerminalRenderAgent.add("Type 'off' to power off your system.")
    LineRenderer.TerminalRenderAgent.add("")
    input()
    applet_off(globals_list)

def applet_reboot(globals_list: list) -> None:
    OnShell = globals_list["OnShell"]
    OnShell.change(0)
    CurrentApp = globals_list["CurrentApp"]
    CurrentApp.change("reboot")
    CurrentFSLocation = globals_list["CurrentFSLocation"]
    CurrentFSLocation.change("REBOOT")
    CurrentUser = globals_list["CurrentUser"]
    LineRenderer = globals_list["LineRenderer"]
    DeviceName = globals_list["DeviceName"]
    real_LFS = globals_list["mounts"]["LFS"]
    linecore_portable = globals_list["linecore_portable"]
    LineRenderer.InputLine.change(
        f"{CurrentUser.get()} | {CurrentFSLocation.get()} @ {DeviceName.get()} :"
    )
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    LineRenderer.TerminalRenderAgent.add(f"Reboot called @ {formatted_time} for system '{DeviceName.get()}'")
    LineRenderer.TerminalRenderAgent.add("Rebooting in 5")
    time.sleep(1)
    LineRenderer.TerminalRenderAgent.remove(len(list(LineRenderer.TerminalRenderAgent)))
    LineRenderer.TerminalRenderAgent.add("Rebooting in 4")
    time.sleep(1)
    LineRenderer.TerminalRenderAgent.remove(len(list(LineRenderer.TerminalRenderAgent)))
    LineRenderer.TerminalRenderAgent.add("Rebooting in 3")
    time.sleep(1)
    LineRenderer.TerminalRenderAgent.remove(len(list(LineRenderer.TerminalRenderAgent)))
    LineRenderer.TerminalRenderAgent.add("Rebooting in 2")
    time.sleep(1)
    LineRenderer.TerminalRenderAgent.remove(len(list(LineRenderer.TerminalRenderAgent)))
    LineRenderer.TerminalRenderAgent.add("Rebooting in 1")
    time.sleep(1)
    LineRenderer.TerminalRenderAgent.remove(len(list(LineRenderer.TerminalRenderAgent)))
    LineRenderer.TerminalRenderAgent.add("Rebooting...")
    time.sleep(1)
    LineRenderer.InputLine.change("default | INIT @ SYSTEM :")
    LineRenderer.TerminalRenderAgent.clear()
    # yes, this is really the way to export to a ZIP on the disk in zipfile. horrible design.
    with zipfile.ZipFile('LFS.zip', 'w') as zip_write:
        for file_info in real_LFS.infolist():
            data = real_LFS.read(file_info.filename)
            zip_write.writestr(file_info, data)
    if linecore_portable:
        # linecoreos by default doesn't clear this when rebooting.
        # enable it for portable mode because when this runs natively the mounts will be gone anyway
        globals_list["LFS"] = None
        globals_list["mounts"] = {"LFS": None}
    # linecore.py NO LONGER! handles the rest
    # SHORE has said that warpix v2 (warpix v1 was 100% different from linecore, warpix v2 is based on linecore) will be monolithic
    # no longer true ^
    # so I don't really care anyway
    if globals_list["native"]:
        globals_list["linative"].reboot()
    globals_list["Function"]()

# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the am applet from LineCore OS in Python."""
import urllib.request
import io
import zipfile

def applet_am(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    OnShell = globals_list["OnShell"]
    mounts = globals_list["mounts"]
    CurrentApp = globals_list["CurrentApp"]
    CurrentFSLocation = globals_list["CurrentFSLocation"]
    DeviceName = globals_list["DeviceName"]
    CurrentUser = globals_list["CurrentUser"]
    linecore_portable = globals_list["linecore_portable"]
    current_cmd = globals_list["current_cmd"].get()
    if current_cmd == "am #help":
        LineRenderer.TerminalRenderAgent.add("AM Help")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("AM works by adding the user specified URL as a mount.")
        LineRenderer.TerminalRenderAgent.add("")
        LineRenderer.TerminalRenderAgent.add("Example Usage:")
        LineRenderer.TerminalRenderAgent.add("'am https://colebohte.github.io/fs/test.zip'")
        return
    if current_cmd == "am" and linecore_portable:
        return
    arg = current_cmd.replace("am ", "")
    OnShell.change(0)
    CurrentApp.change("am")
    CurrentFSLocation.change("AM")
    LineRenderer.InputLine.change(f"{CurrentUser.get()} | {CurrentFSLocation.get()} @ {DeviceName.get()} :")
    LineRenderer.TerminalRenderAgent.add("Choose a name for the mount:")
    mount_name = input("")
    LineRenderer.TerminalRenderAgent.add(f"{CurrentUser.get()} | {CurrentFSLocation.get()} @ {DeviceName.get()} : {mount_name}")
    with urllib.request.urlopen(arg) as response:
        mount_zip = zipfile.ZipFile(io.BytesIO(response.read()))
    mounts[mount_name] = mount_zip
    # TODO: unhardcode everything from LFS so we don't have to do this
    # although, this is what linecore does normally [Sprite: applets//am], so who cares
    globals_list["LFS"] = mounts["LFS"]
    # reset pwd, don't want to break the lineshell
    # although sm does this as well(?) so no problems here
    if mount_name == "LFS":
        globals_list["pwd"] = ""
    LineRenderer.TerminalRenderAgent.add(f"AM: Added mount '{mount_name}/'")
    LineRenderer.TerminalRenderAgent.add(f"AM: To switch to this mount use 'sm {mount_name}'")

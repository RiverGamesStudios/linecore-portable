# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Tools that applets can use."""
import zipfile
import io

def create_dir(zipfileformat, name: str) -> None:
    zipfileformat.writestr(f"{name}/", b"")

def delete_dir(zipfileformat, name: str) -> zipfile.ZipFile:
    # yes, this is really the way to delete folders in zipfile. horrible design.
    new_LFS = zipfile.ZipFile(io.BytesIO(), "w")
    for item in zipfileformat.infolist():
        if not item.filename.startswith(name):
            new_LFS.writestr(item, zipfileformat.read(item.filename))
    zipfileformat.close()
    return new_LFS

def delete_file(zipfileformat, name: str) -> zipfile.ZipFile:
    # yes, this is really the way to delete files in zipfile. horrible design.
    new_LFS = zipfile.ZipFile(io.BytesIO(), "w")
    for item in zipfileformat.infolist():
        if not item.filename == name:
            new_LFS.writestr(item, zipfileformat.read(item.filename))
    zipfileformat.close()
    return new_LFS

def db_to_use(globals_list: list) -> zipfile.ZipFile:
    """
    Get current mount.
    Use only for applets related to administrative actions.
    Example: `setup`
    Non-example: `write`
    """
    linecore_portable = globals_list["linecore_portable"]
    if linecore_portable:
        return globals_list["mounts"]["LFS"]
    return globals_list["LFS"]

def update_ps1(globals_list: list) -> None:
    """Updates the PS1."""
    LineRenderer = globals_list["LineRenderer"]
    CurrentFSLocation = globals_list["CurrentFSLocation"]
    CurrentUser = globals_list["CurrentUser"]
    DeviceName = globals_list["DeviceName"]
    LineRenderer.InputLine.change(f"{CurrentUser.get()} | {CurrentFSLocation.get()} @ {DeviceName.get()} :")

def does_file_exist(mount: zipfile.ZipFile, file: str) -> bool:
    checkparser = zipfile.Path(mount, file)
    return checkparser.exists()

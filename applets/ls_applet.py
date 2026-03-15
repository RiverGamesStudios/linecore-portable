# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the ls applet from LineCore OS in Python."""
import zipfile

def applet_ls(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    LFS = globals_list["LFS"]
    pwd = globals_list["pwd"]
    CurrentFSLocation = globals_list["CurrentFSLocation"].get()
    LineRenderer.TerminalRenderAgent.add(f"Directory of '{CurrentFSLocation}'")
    filepath = zipfile.Path(LFS, pwd)
    dirs = list(filepath.iterdir())
    names = []
    for directory in dirs:
        if directory.is_dir():
            names.append(f"{directory.name}/")
        else:
            names.append(f"{directory.name}")
    for name in names:
        LineRenderer.TerminalRenderAgent.add(name)

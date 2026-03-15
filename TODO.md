* ~~Finish up `write`~~
* Fix LFS hardcoded stuff to use `db_to_use`,
    ```python
    if linecore_portable:
        db_to_use = globals_list["mounts"]["LFS"]
    else:
        db_to_use = globals_list["LFS"]
    ```
* Modular applet system
* ~~Move reboot features to inside of the applet~~
* ~~Automatically reset OnShell state after applet quits in `shell_input()`~~
* Migrate stuff to libapplet
* Stop using .replace() for removing beginning of applet **in portable mode**
* ~~Handle ^C in `shell_input()` literally as easy as putting~~
    ```python
    except KeyboardInterrupt:
        pass
    ```
* Make sure to decode everything after `.read()`ing the file from the ZIP
* Add multi-line `write` in portable mode
* Make a package manager, similar to grab
* Package for GNU variants
* Support multiple LineRenderer backends (similar to post-warpix)

<!--
SPDX-License-Identifier: CC0-1.0
SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
-->

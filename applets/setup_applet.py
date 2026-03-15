# SPDX-License-Identifier: GPL-2.0-or-later OR MIT
# SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan
"""Reimplementation of the setup applet from LineCore OS in Python."""
import hashlib
import zipfile
import io
import urllib.request
import applets.libapplet

def applet_setup(globals_list: list) -> None:
    LineRenderer = globals_list["LineRenderer"]
    linecore_portable = globals_list["linecore_portable"]
    globals_list["OnShell"].change(0)
    CurrentApp = globals_list["CurrentApp"]
    CurrentApp.change("setup")
    CurrentFSLocation = globals_list["CurrentFSLocation"]
    CurrentFSLocation.change("SETUP")
    DeviceName = globals_list["DeviceName"]
    CurrentUser = globals_list["CurrentUser"]
    applets.libapplet.update_ps1(globals_list)
    page = ""
    try:
        while True:
            if page == "":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("List of Configurable Settings:")
                LineRenderer.TerminalRenderAgent.add("1 - User Setup")
                LineRenderer.TerminalRenderAgent.add("2 - System Basics")
                LineRenderer.TerminalRenderAgent.add("3 - Display & UI")
                LineRenderer.TerminalRenderAgent.add("4 - Security")
                LineRenderer.TerminalRenderAgent.add("5 - Storage & LineFS")
                LineRenderer.TerminalRenderAgent.add("6 - Advanced")
                LineRenderer.TerminalRenderAgent.add("7 - About")
                LineRenderer.TerminalRenderAgent.add("")
                # TODO: Fix ^C in all `input()`s in applets
                LineRenderer.TerminalRenderAgent.add("^C - Exit")
                LineRenderer.TerminalRenderAgent.add("")
                choice = input("")
                if choice == "1":
                    page = "1"
                if choice == "2":
                    page = "2"
                if choice == "3":
                    page = "3"
                if choice == "4":
                    page = "4"
                if choice == "5":
                    page = "5"
                if choice == "6":
                    page = "6"
                if choice == "7":
                    page = "7"
            elif page == "1":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > User Setup")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("List of Configurable Settings:")
                LineRenderer.TerminalRenderAgent.add("a - Create User")
                LineRenderer.TerminalRenderAgent.add("b - Remove User")
                LineRenderer.TerminalRenderAgent.add("c - Back")
                LineRenderer.TerminalRenderAgent.add("")
                choice = input("")
                if choice == "a":
                    page = "1:1"
                if choice == "b":
                    page = "1:2"
                if choice == "c":
                    page = ""
            elif page == "1:1":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > User Setup > Create User")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("Type Username:")
                # there's no way to check for HOLDING enter
                # so we will just remove this part in portable mode
                # but we have to keep compatibility, of course
                if linecore_portable:
                    LineRenderer.TerminalRenderAgent.add("(Press ENTER to confirm)")
                else:
                    LineRenderer.TerminalRenderAgent.add("(Press and hold ENTER to confirm)")
                choice = input("")
                # SHORE said it's supposed to go to LFS/users
                # but by default it goes to current_mount/users
                if linecore_portable:
                    db_to_use = globals_list["mounts"]["LFS"]
                else:
                    db_to_use = globals_list["LFS"]
                applets.libapplet.create_dir(db_to_use, f"/user/{choice}")
                applets.libapplet.create_dir(db_to_use, f"/user/{choice}/Applets")
                applets.libapplet.create_dir(db_to_use, f"/user/{choice}/Documents")
                applets.libapplet.create_dir(db_to_use, f"/opt/userdata/{choice}")
                db_to_use.writestr(f"/opt/userdata/{choice}/bgcolour.pref", "#000000")
                db_to_use.writestr(f"/opt/userdata/{choice}/textcolour.pref", "#FFFFFF")
                db_to_use.writestr(f"/opt/userdata/{choice}/textcursor.pref", "_")
                db_to_use.writestr(f"/opt/userdata/{choice}/presshold.pref", "0.3")
                if not linecore_portable:
                    # this should not be written, as it overrides the original contents
                    db_to_use.writestr("/opt/systemdata/region.pref", "International")
                db_to_use.writestr(f"/opt/userdata/{choice}/user.pwrd", hashlib.sha256("password".encode()).hexdigest())
                db_to_use.writestr(f"/opt/userdata/{choice}/pwrdenabled.pref", "false")
                page = "1"
            elif page == "1:2":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > User Setup > Remove User")
                if linecore_portable:
                    db_to_use = globals_list["mounts"]["LFS"]
                else:
                    db_to_use = globals_list["LFS"]
                userdir = zipfile.Path(db_to_use, "user/")
                users_dirs = [i.name for i in userdir.iterdir()]
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add(f"Registered Users: {' '.join(users_dirs)}")
                LineRenderer.TerminalRenderAgent.add("Type Username to Delete (Omit forward slash):")
                if linecore_portable:
                    LineRenderer.TerminalRenderAgent.add("(Press ENTER to confirm)")
                else:
                    LineRenderer.TerminalRenderAgent.add("(Press and hold ENTER to confirm)")
                choice = input("")
                new_LFS = applets.libapplet.delete_dir(db_to_use, f"/user/{choice}/")
                new_LFS = applets.libapplet.delete_dir(new_LFS, f"/opt/userdata/{choice}/")
                if linecore_portable:
                    globals_list["mounts"]["LFS"] = new_LFS
                else:
                    globals_list["LFS"] = new_LFS
                page = "1"
            elif page == "2":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > System Basics")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("List of Configurable Settings:")
                LineRenderer.TerminalRenderAgent.add("a - Modify Device Name")
                LineRenderer.TerminalRenderAgent.add("b - Modify Region")
                LineRenderer.TerminalRenderAgent.add("c - Back")
                LineRenderer.TerminalRenderAgent.add("")
                choice = input("")
                if choice == "a":
                    page = "2:1"
                if choice == "b":
                    page = "2:2"
                if choice == "c":
                    page = ""
            elif page == "2:1":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > System Basics > Modify Device Name")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add(f"Current Device Name: {DeviceName.get()}")
                LineRenderer.TerminalRenderAgent.add("Type new device name:")
                if linecore_portable:
                    LineRenderer.TerminalRenderAgent.add("(Press ENTER to confirm)")
                else:
                    LineRenderer.TerminalRenderAgent.add("(Press and hold ENTER to confirm)")
                choice = input("")
                if linecore_portable:
                    db_to_use = globals_list["mounts"]["LFS"]
                else:
                    db_to_use = globals_list["LFS"]
                db_to_use.writestr("/opt/systemdata/devicename.pref", choice)
                page = "2"
            elif page == "2:2":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > System Basics > Modify Default Prompt Location")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("Default: International")
                if linecore_portable:
                    db_to_use = globals_list["mounts"]["LFS"]
                else:
                    db_to_use = globals_list["LFS"]
                with db_to_use.open("opt/systemdata/region.pref", "r") as f:
                    LineRenderer.TerminalRenderAgent.add(f"Current Region: {f.read().decode()}")
                LineRenderer.TerminalRenderAgent.add("Type region as a country (ex. Canada):")
                if linecore_portable:
                    LineRenderer.TerminalRenderAgent.add("(Press ENTER to confirm)")
                else:
                    LineRenderer.TerminalRenderAgent.add("(Press and hold ENTER to confirm)")
                choice = input("")
                db_to_use.writestr("/opt/systemdata/region.pref", choice)
                page = "2"
            elif page == "3":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > Display & UI")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("List of Configurable Settings:")
                LineRenderer.TerminalRenderAgent.add("a - Change Text Colour")
                LineRenderer.TerminalRenderAgent.add("b - Change Background Colour")
                LineRenderer.TerminalRenderAgent.add("c - Modify Text Cursor")
                LineRenderer.TerminalRenderAgent.add("d - Back")
                LineRenderer.TerminalRenderAgent.add("")
                choice = input("")
                if choice == "a":
                    page = "3:1"
                if choice == "b":
                    page = "3:2"
                if choice == "c":
                    page = "3:3"
                if choice == "d":
                    page = ""
            elif page == "3:1":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > Display & UI > Change Text Colour")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("Default: #FFFFFF")
                LineRenderer.TerminalRenderAgent.add("Type colour as HEX value (ex. #FFFF55):")
                if linecore_portable:
                    LineRenderer.TerminalRenderAgent.add("(Press ENTER to confirm)")
                else:
                    LineRenderer.TerminalRenderAgent.add("(Press and hold ENTER to confirm)")
                choice = input("")
                if linecore_portable:
                    db_to_use = globals_list["mounts"]["LFS"]
                else:
                    db_to_use = globals_list["LFS"]
                db_to_use.writestr(f"/opt/userdata/{CurrentUser.get()}/textcolour.pref", choice)
                page = "3"
            elif page == "3:2":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > Display & UI > Change Background Colour")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("Default: #000000")
                LineRenderer.TerminalRenderAgent.add("Type colour as HEX value (ex. #012456):")
                if linecore_portable:
                    LineRenderer.TerminalRenderAgent.add("(Press ENTER to confirm)")
                else:
                    LineRenderer.TerminalRenderAgent.add("(Press and hold ENTER to confirm)")
                choice = input("")
                if linecore_portable:
                    db_to_use = globals_list["mounts"]["LFS"]
                else:
                    db_to_use = globals_list["LFS"]
                db_to_use.writestr(f"/opt/userdata/{CurrentUser.get()}/bgcolour.pref", choice)
                page = "3"
            elif page == "3:3":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > Display & UI > Modify Text Cursor")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("Default: _")
                LineRenderer.TerminalRenderAgent.add("Type a character (ex. #):")
                if linecore_portable:
                    LineRenderer.TerminalRenderAgent.add("(Press ENTER to confirm)")
                else:
                    LineRenderer.TerminalRenderAgent.add("(Press and hold ENTER to confirm)")
                choice = input("")
                if linecore_portable:
                    db_to_use = globals_list["mounts"]["LFS"]
                else:
                    db_to_use = globals_list["LFS"]
                db_to_use.writestr(f"/opt/userdata/{CurrentUser.get()}/textcursor.pref", choice)
                page = "3"
            elif page == "4":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > Security")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("List of Configurable Settings:")
                LineRenderer.TerminalRenderAgent.add("a - Enable/Disable Password")
                LineRenderer.TerminalRenderAgent.add("b - Change Password")
                LineRenderer.TerminalRenderAgent.add("c - Back")
                LineRenderer.TerminalRenderAgent.add("")
                choice = input("")
                if choice == "a":
                    page = "4:1"
                if choice == "b":
                    page = "4:2"
                if choice == "c":
                    page = ""
            elif page == "4:1":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > Security > Enable/Disable Password")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("Default: false")
                if linecore_portable:
                    db_to_use = globals_list["mounts"]["LFS"]
                else:
                    db_to_use = globals_list["LFS"]
                with db_to_use.open(f"opt/userdata/{CurrentUser.get()}/pwrdenabled.pref", "r") as f:
                    LineRenderer.TerminalRenderAgent.add(f"Current Value: {f.read().decode()}")
                LineRenderer.TerminalRenderAgent.add("Type 'true' or 'false':")
                if linecore_portable:
                    LineRenderer.TerminalRenderAgent.add("(Press ENTER to confirm)")
                else:
                    LineRenderer.TerminalRenderAgent.add("(Press and hold ENTER to confirm)")
                choice = input("")
                if choice != "true" and choice != "false" and linecore_portable:
                    LineRenderer.TerminalRenderAgent.add("Invalid input")
                else:
                    db_to_use.writestr(f"/opt/userdata/{CurrentUser.get()}/pwrdenabled.pref", choice)
                page = "4"
            elif page == "4:2":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > Security > Change Password")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("Default: password")
                if linecore_portable:
                    db_to_use = globals_list["mounts"]["LFS"]
                else:
                    db_to_use = globals_list["LFS"]
                with db_to_use.open(f"opt/userdata/{CurrentUser.get()}/pwrdenabled.pref", "r") as f:
                    LineRenderer.TerminalRenderAgent.add(f"Password Enabled: {f.read().decode()}")
                LineRenderer.TerminalRenderAgent.add("Type a password:")
                if linecore_portable:
                    LineRenderer.TerminalRenderAgent.add("(Press ENTER to confirm)")
                else:
                    LineRenderer.TerminalRenderAgent.add("(Press and hold ENTER to confirm)")
                choice = input("")
                db_to_use.writestr(f"/opt/userdata/{CurrentUser.get()}/user.pwrd", hashlib.sha256(choice.encode()).hexdigest())
                page = "4"
            elif page == "5":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > Storage & LineFS")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("List of Configurable Settings:")
                LineRenderer.TerminalRenderAgent.add("a - Download LineFS Data")
                LineRenderer.TerminalRenderAgent.add("b - Load FS via HTTPS")
                LineRenderer.TerminalRenderAgent.add("c - Back")
                LineRenderer.TerminalRenderAgent.add("")
                if linecore_portable:
                    db_to_use = globals_list["mounts"]["LFS"]
                else:
                    db_to_use = globals_list["LFS"]
                choice = input("")
                if choice == "a":
                    # yes, this is really the way to export to a ZIP on the disk in zipfile. horrible design.
                    with zipfile.ZipFile('LFS.zip', 'w') as zip_write:
                        for file_info in db_to_use.infolist():
                            data = db_to_use.read(file_info.filename)
                            zip_write.writestr(file_info, data)
                if choice == "b":
                    page = "5:1"
                if choice == "c":
                    page = ""
            elif page == "5:1":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > Storage & LineFS > Load FS via HTTPS")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("* Warning *")
                LineRenderer.TerminalRenderAgent.add("The screen may go blank for a couple of seconds as the File System reloads.")
                if linecore_portable:
                    LineRenderer.TerminalRenderAgent.add("To cancel, type nothing and press ENTER.")
                else:
                    LineRenderer.TerminalRenderAgent.add("To cancel, type nothing and hold ENTER.")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("Type a valid URL that leads to a LineFS zip archive (ex. https://colebohte.github.io/fs/linefs.zip/):")
                if linecore_portable:
                    LineRenderer.TerminalRenderAgent.add("(Press ENTER to confirm)")
                else:
                    LineRenderer.TerminalRenderAgent.add("(Press and hold ENTER to confirm)")
                choice = input("")
                globals_list["mounts"]["LFS"].close()
                with urllib.request.urlopen(choice) as response:
                    mount_zip = zipfile.ZipFile(io.BytesIO(response.read()))
                globals_list["mounts"]["LFS"] = mount_zip
                page = "5"
            elif page == "6":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > Advanced")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("List of Configurable Settings:")
                LineRenderer.TerminalRenderAgent.add("a - Reset LineCoreOS")
                LineRenderer.TerminalRenderAgent.add("b - Back")
                LineRenderer.TerminalRenderAgent.add("")
                choice = input("")
                if choice == "a":
                    page = "6:1"
                if choice == "b":
                    page = ""
            elif page == "6:1":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > Advanced  > Reset LineCoreOS")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("Are you sure you want to delete ALL user generated data on drive 'LFS'?")
                LineRenderer.TerminalRenderAgent.add("To delete ALL data, type 'I would like to proceed with deletion'. To cancel, type anything else.")
                if linecore_portable:
                    LineRenderer.TerminalRenderAgent.add("(Press ENTER to confirm)")
                else:
                    LineRenderer.TerminalRenderAgent.add("(Press and hold ENTER to confirm)")
                choice = input("")
                if choice == "I would like to proceed with deletion":
                    globals_list["mounts"]["LFS"].close()
                    globals_list["mounts"]["LFS"] = None
                    if globals_list["current_mount"] == "LFS":
                        globals_list["LFS"] = None
                    # we can't pass it on back to linecore.py
                    # so this is required
                    globals_list["Function"]()
                else:
                    page = "6"
            elif page == "7":
                LineRenderer.TerminalRenderAgent.clear()
                LineRenderer.TerminalRenderAgent.add("LineCoreOS Setup Utility > About")
                LineRenderer.TerminalRenderAgent.add("")
                SetupUtilityVer = globals_list["SetupUtilityVer"].get()
                SystemSoftwareVer = globals_list["SystemSoftwareVer"].get()
                LineRenderer.TerminalRenderAgent.add(f"LineCoreOS Setup Utility v{SetupUtilityVer}")
                LineRenderer.TerminalRenderAgent.add(f"LineCoreOS v{SystemSoftwareVer}")
                LineRenderer.TerminalRenderAgent.add(f"LineKernel v{SystemSoftwareVer}")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("LineKernel, LineCoreOS, LineShell & LineShell")
                LineRenderer.TerminalRenderAgent.add("Developed by colebohte @ River Games: Shore Division")
                if linecore_portable:
                    LineRenderer.TerminalRenderAgent.add("LineCore Portable")
                    LineRenderer.TerminalRenderAgent.add("Developed by NexusSfan @ River Games: Tsunami Division")
                    LineRenderer.TerminalRenderAgent.add("SPDX-License-Identifier: GPL-2.0-or-later OR MIT")
                    LineRenderer.TerminalRenderAgent.add("SPDX-FileCopyrightText: Copyright (C) 2026 NexusSfan")
                LineRenderer.TerminalRenderAgent.add("")
                LineRenderer.TerminalRenderAgent.add("a - Back")
                LineRenderer.TerminalRenderAgent.add("")
                choice = input("")
                if choice == "a":
                    page = ""
    except KeyboardInterrupt:
        globals_list["OnShell"].change(True)
        return

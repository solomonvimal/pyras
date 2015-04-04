# Copyright (c) 1996-2008, Greg Stein and Mark Hammond.

import win32api
import win32con


def get_typelib_info(keyid, version):
        collected = []
        help_path = ""
        key = win32api.RegOpenKey(win32con.HKEY_CLASSES_ROOT,
                                  "TypeLib\\%s\\%s" % (keyid, version))
        try:
            num = 0
            while 1:
                try:
                    sub_key = win32api.RegEnumKey(key, num)
                except win32api.error:
                    break
                h_sub_key = win32api.RegOpenKey(key, sub_key)
                try:
                    value, typ = win32api.RegQueryValueEx(h_sub_key, None)
                    if typ == win32con.REG_EXPAND_SZ:
                        value = win32api.ExpandEnvironmentStrings(value)
                except win32api.error:
                    value = ""
                if sub_key == "HELPDIR":
                    help_path = value
                elif sub_key == "Flags":
                    flags = value
                else:
                    try:
                        lcid = int(sub_key)
                        lcidkey = win32api.RegOpenKey(key, sub_key)
                        # Enumerate the platforms
                        lcidnum = 0
                        while 1:
                            try:
                                platform = win32api.RegEnumKey(lcidkey, lcidnum)
                            except win32api.error:
                                break
                            try:
                                hplatform = win32api.RegOpenKey(lcidkey, platform)
                                fname, typ = win32api.RegQueryValueEx(hplatform, None)
                                if typ == win32con.REG_EXPAND_SZ:
                                    fname = win32api.ExpandEnvironmentStrings(fname)
                            except win32api.error:
                                fname = ""
                            collected.append((lcid, platform, fname))
                            lcidnum = lcidnum + 1
                        win32api.RegCloseKey(lcidkey)
                    except ValueError:
                        pass
                num = num + 1
        finally:
            win32api.RegCloseKey(key)

        return fname


def get_registered_typelibs(match='HEC River Analysis System'):
    """ """
    # Explicit lookup in the registry.
    result = []
    key = win32api.RegOpenKey(win32con.HKEY_CLASSES_ROOT, "TypeLib")
    try:
        num = 0
        while 1:
            try:
                key_name = win32api.RegEnumKey(key, num)
            except win32api.error:
                break
            # Enumerate all version info
            sub_key = win32api.RegOpenKey(key, key_name)
            name = None
            try:
                sub_num = 0
                best_version = 0.0
                while 1:
                    try:
                        version_str = win32api.RegEnumKey(sub_key, sub_num)
                    except win32api.error:
                        break
                    try:
                        version_flt = float(version_str)
                    except ValueError:
                        version_flt = 0  # ????
                    if version_flt > best_version:
                        best_version = version_flt
                        name = win32api.RegQueryValue(sub_key, version_str)
                    sub_num = sub_num + 1
            finally:
                win32api.RegCloseKey(sub_key)
            if name is not None and match in name:
                fname = get_typelib_info(key_name, version_str)
                result.append((name, version_str, key_name, fname))
            num = num + 1
    finally:
        win32api.RegCloseKey(key)
    result = sorted(result)
    return result

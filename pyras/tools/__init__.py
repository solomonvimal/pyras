# Copyright (c) 1996-2008, Greg Stein and Mark Hammond.

import os

import win32api
import win32con


from runtime import Runtime


def get_available_versions():
    """ """
    ver = {'HEC-RAS\\4.1.0\\ras.exe': 'RAS41',
           'HEC-RAS\\5.0 Beta 2014-10-01\\ras.exe': 'RAS500'}

    ldic = get_registered_typelibs()

    # Check if files actually exist (another sanity check)
    available_versions = []

    for dic in ldic:
        fname = dic['filename']
        if os.path.isfile(fname):
            for k in ver:
                if k in fname:
                    available_versions.append(ver[k])
    return available_versions


def get_supported_versions():
    """ """
    # Order is important as it gives the priority
    return ['RAS500', 'RAS41']


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

        return fname, lcid


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
                fname, lcid = get_typelib_info(key_name, version_str)

                # Split version
                major, minor = version_str.split('.')

                result.append({'name': name,
                               'filename': fname,
                               'iid': key_name,
                               'lcid': lcid,
                               'major': int(major),
                               'minor': int(minor)})
            num = num + 1
    finally:
        win32api.RegCloseKey(key)
    result = sorted(result)
    return result

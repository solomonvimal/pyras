"""
PyRAS
=====


"""
import os
import subprocess

from .tools import get_available_versions, get_supported_versions


__version__ = '0.1.0'
_available_versions = get_available_versions()


def kill_all():
    """ """
    import os
    ras_process_string = 'ras.exe'
    proc = subprocess.Popen('TASKLIST /FO "CSV"', stdout=subprocess.PIPE)
    tasklist = proc.stdout.read().split('\n')
    tasks = []
    pids = []
    for line in tasklist:
        l = line.lower()
        if ras_process_string in l:
            items = l.split(',')
            tasks.append(items)
            pids.append(int(eval(items[1])))

    for pid in pids:
        try:
            killed = os.system('TASKKILL /PID {0} /F >nul'.format(pid))
        except Exception, e:
            #print(e)
            killed = 0

kill_all()

if len(_available_versions) > 0:
    for ras_version in get_supported_versions():
        if ras_version in _available_versions:
            os.environ['RAS_CONTROLLER_VERSION'] = ras_version
            break

#        try:
#            os.environ['RAS_CONTROLLER_VERSION'] = ras_version
#            from .hecrascontroller import HECRASController
#            from .pyras import PyRAS
#
#            rc = HECRASController(ras_version)
#            rc.close()
#            _available_versions.append(ras_version)
#        except Exception:
#            pass

    from .hecrascontroller import HECRASController
    from .pyras import PyRAS

    # Cleaning the namespace
    globals().pop('hecrascontroller')
    globals().pop('hecrasgeometry')
    globals().pop('pyras')
    globals().pop('tools')
else:
    error = '"HEC River Analysis System" type library not found. ' \
            'Please install HEC-RAS'
    raise Exception(error)

import os
import _winreg


def get_python_executables():
    """
    Find the Maya installation paths using _winreg. The path to the python
    executable is extended from the installation path. The dictionary is made
    up of keys that are made up of the Maya versions found installed and a 
    path to the executable of that version of Maya as a value.
    
    :return: Windows maya python executables
    :rtype: dict
    """
    # variables
    maya_pythons = {}
    
    registry = _winreg.HKEY_LOCAL_MACHINE
    registry_maya_path = r"SOFTWARE\Autodesk\Maya"

    # get maya key
    maya_key_data = [
        registry, 
        registry_maya_path, 
        0, 
        _winreg.KEY_READ
    ]

    with _winreg.OpenKey(*maya_key_data) as maya_key:
        # loop keys
        for i in xrange(0, _winreg.QueryInfoKey(maya_key)[0]):
            # get version
            maya_version = _winreg.EnumKey(maya_key, i)
            
            # validate version
            if not maya_version.split(".")[0].isdigit():
                continue
               
            # get install path
            registry_maya_install_path = os.path.join(
                registry_maya_path, maya_version, "Setup", "InstallPath"
            )
            
            # get install key
            maya_install_key_data = [
                registry, 
                registry_maya_install_path, 
                0, 
                _winreg.KEY_READ
            ]
            
            with _winreg.OpenKey(*maya_install_key_data) as maya_install_key:
                # get path
                maya_location_data = [maya_install_key, "MAYA_INSTALL_LOCATION"]
                maya_location = _winreg.QueryValueEx(*maya_location_data)[0]
                
                # set data
                maya_py = os.path.join(maya_location, "bin", "mayapy.exe")
                maya_pythons[maya_version] = maya_py

    return maya_pythons

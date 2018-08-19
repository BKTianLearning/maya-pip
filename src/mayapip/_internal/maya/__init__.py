import platform

# declare variable in case operating system is not supported
get_python_executables = None


# get maya python executables based on platform
if platform.system() == "Windows":
    from .maya_windows import get_python_executables
elif platform.system() == "Linux":
    from .maya_linux import get_python_executables
    
    
def has_python_executables():
    return True \
        if get_python_executables and get_python_executables() \
        else False

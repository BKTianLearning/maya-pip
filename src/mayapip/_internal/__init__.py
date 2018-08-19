#!/usr/bin/env python
from __future__ import absolute_import

import os
import sys
import argparse
import subprocess

from pip._internal import parseopts
from mayapip._internal import maya


def main(args=None):
    # get arguments
    if args is None:
        args = sys.argv[1:]
        
    # parse arguments
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--maya_version", type=str)
    maya_args, pip_args = parser.parse_known_args(args)
        
    # validate pip arguments
    parseopts(pip_args)
    
    # get maya python executables
    python_executables = maya.get_python_executables()
    
    # catch no executables found at all
    if not maya.has_python_executables():
        raise RuntimeError("No installed versions of Maya found.")
        
    # handle maya versions
    maya_version =  maya_args.maya_version
    maya_versions = python_executables.keys()
    maya_versions.sort()
    maya_versions_string = ", ".join(maya_versions)
    
    # catch no maya version specified, but more than one version installed.
    if not maya_version and len(python_executables) > 1:
        message = (
            "Multiple versions of Maya found ({0}).\n"
            "Use the --maya_version argument to "
            "specify the version you would with to use."
        ).format(maya_versions_string)
        
        raise RuntimeError(message)
        
    # catch maya version specified, but version not installed
    elif maya_version and maya_version not in maya_versions:
        message = (
            "Specified version of Maya is not found.\n"
            "Use one of the following versions ({0})"
        ).format(maya_versions_string)
        
        raise RuntimeError(message)
        
    # execute
    maya_version = maya_version if maya_version else maya_versions[0]
    executable = python_executables.get(maya_version)
    
    subprocess.call(
        [executable, "-m", "pip"] + pip_args,
        cwd=os.getcwd()
    )

mayapip
=======

The Maya tool for installing Python packages.

Installation
------------

Using pip:

    pip install <TAR>

If you prefer to install from source code use:

    cd maya-pip/
    python setup.py install

Usage
-----

This tool is a wrapper around pip. The tool will find the Maya python 
executables and uses those to execute the pip command. Using the Maya python
executables the packages will be installed in the site-packages directory of 
the chosen version of Maya.

From the command line:

    mayapip -h              will print the default help from the pip command
    
    Additional arguments:
	--maya_version:         which version of Maya to use ( only needs to be provided if multiple version of Maya are installed )

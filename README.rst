mayapip
=======

The Maya wrapper to pip_ for installing Python packages.

Installation
------------

Using pip:

::

    pip install https://github.com/robertjoosten/maya-pip/archive/v0.1.2.tar.gz

If you prefer to install from source code use:

::

    cd maya-pip
    python setup.py install

Usage
-----

This tool is a wrapper around pip. The tool will find the Maya python 
executables and uses it to execute the pip command. By using the Maya python
executable the packages will be installed in the site-packages directory of 
the chosen version of Maya.

Command line:

**mayapip**

-h            	will print the default help from the pip command
--maya_version	which version of Maya to use ( only needs to be provided if multiple version of Maya are installed )

Limitations
-----------

At the moment this version of mayapip will only work on Windows, this is 
because I dont have any of the other platforms at my disposal. Feel free
to implement solution for Mac and Linux in the maya directory and submit
a pull request.

Examples
--------

Installing an older version of pyyaml on Maya 2017.

::

    mayapip install pyyaml==3.11 --maya_version=2017
    >>> Successfully installed pyyaml-3.11

    # in maya 2017
    import yaml 

    print yaml.__version__
    print yaml.__file__
    >>> 3.11
    >>> C:\Program Files\Autodesk\Maya2017\Python\lib\site-packages\yaml\__init__.pyc

Installing the latest version of pyyaml on Maya 2018.

::

    mayapip install pyyaml --maya_version=2018
    >>> Successfully installed pyyaml-3.13

    # in maya 2018
    import yaml

    print yaml.__version__
    print yaml.__file__
    >>> 3.13
    >>> C:\Program Files\Autodesk\Maya2018\Python\lib\site-packages\yaml\__init__.pyc
	
Uninstalling pyyaml from Maya 2018, leaving the Maya 2017 environment intact.
	
::

    mayapip uninstall pyyaml --maya_version=2018
    >>> Successfully uninstalled PyYAML-3.13
	
.. _pip: https://github.com/pypa/pip

import codecs
import os
import re
import sys

from setuptools import find_packages, setup


# ----------------------------------------------------------------------------


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

        
def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")
  
  
here = os.path.abspath(os.path.dirname(__file__))  
long_description = read("README.rst")

    
# ----------------------------------------------------------------------------    
    

setup(
    name="mayapip",
    version=find_version("src", "mayapip", "__init__.py"),
    author="Robert Joosten",
    author_email="rwm.joosten@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        exclude=["contrib", "docs", "tests*", "tasks"],
    ),
    license="MIT",
    description="The Maya wrapper to pip for installing Python packages",
    long_description=long_description,
    keywords="pip maya",
    entry_points={
        "console_scripts": [
            "mayapip=mayapip._internal:main",
        ]
    }
)

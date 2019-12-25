import os
import platform
import sys
from distutils.command.build import build

import pkg_resources

import setuptools
from setuptools import setup, find_packages

print(find_packages(where="src"))
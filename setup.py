#!/usr/bin/env python

import re
import setuptools
import sys


setuptools.setup(
    setup_requires=['pbr', 'pytest-runner'],
    tests_require=['pytest'],
    pbr=True)

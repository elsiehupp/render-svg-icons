#!/usr/bin/python3
# coding: utf-8
#
# Original Version Copyright (C) by the GNOME icon developers
#
# Modifications Copyright (C) by Moka Icon Theme developers
# Modifications Copyright (C) by Yaru Icon Theme developers
# Modifications Copyright (C) by Elsie Hupp <gpl at elsiehupp dot com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.

import os
import sys

from pathlib import Path

class InkscapePath(Path):

    def __init__(self):
        pass

class OptiPngPath(Path):

    def __init__(self):
        pass

class OutputPath(Path):

    def __init__(self):
        pass

class Dependencies:

    _instance: any = None

    _inkscape_path: InkscapePath
    _optipng_path: OptiPngPath
    _output_path: OutputPath

    def __init__(
        self,
        inkscape_path: str,
        optipng_path: str,
        output_path: str):

        # assert ('linux' in sys.platform), "This code runs on Linux only."
        if sys.platform.startswith('linux'):
            assert (os.path.isfile(inkscape_path)), "Expected to find Inkscape at " + inkscape_path + ", but file does not exist." + "\nInstall Inkscape with, e.g., 'apt install inkscape' in order to proceed."
            assert (os.path.isfile(optipng_path)), "Expected to find OptiPNG at " + optipng_path + " but file does not exist." + "\nInstall OptiPNG with, e.g., 'apt install optipng' in order to proceed."
        elif sys.platform.startswith('darwin'):
            assert (os.path.isfile(inkscape_path)), "Expected to find Inkscape at " + inkscape_path + ", but file does not exist." + "\nInstall Inkscape with, e.g., 'brew install inkscape' in order to proceed."
            assert (os.path.isfile(optipng_path)), "Expected to find OptiPNG at " + optipng_path + " but file does not exist." + "\nInstall OptiPNG with, e.g., 'brew install optipng' in order to proceed."
        # assert (os.path.isdir(output_path)), "Expected to find output directory at " + output_path + ", but directory does not exist."

        self._inkscape_path = inkscape_path
        self._optipng_path = optipng_path
        self._output_path = output_path

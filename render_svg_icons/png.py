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

import subprocess

from .dependencies import OptiPngPath

class PngFile:

    _path: str

    def __init__(
        self,
        path: str):

        self._path = path

    def optimize(self):

        process = subprocess.Popen([OptiPngPath(), '-quiet', '-o7', self.path])
        process.wait()
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

from .png import PngFile

class Render:

    def __init__(
        icon_file,
        rect,
        dpi,
        output_file: PngFile):

        cmd = ["inkscape",
            "--batch-process",
            '--export-dpi={}'.format(str(dpi)),
            '--export-id={}'.format(str(rect)),
            '--export-filename={}'.format(output_file),
            icon_file]

        ret = subprocess.run(cmd, capture_output=True)
        if ret.returncode != 0:
            print("execution of")
            print('  %s' % "".join(cmd))
            print("returned with error %d" % ret.returncode)
            print(5*"=", "stdout", 5*"=")
            print(ret.stdout.decode())
            print(5*"=", "stderr", 5*"=")
            print(ret.stderr.decode())
            return

        output_file.optimize()
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

from .render import Render

class Output:

    new_renders: int = 0
    updated_renders: int = 0
    skipped_renders: int = 0

    def __init__(
        context: str,
        rect_id,
        output_path: str,
        size_str: str,
        icon_name: str,
        path: str,
        dpi,
        force: bool,
        verbose: bool):

        dir = os.path.join(output_path, context, size_str)
        outfile = os.path.join(dir, icon_name+'.png')
        if not os.path.exists(dir):
            os.makedirs(dir)

        # If PNG does not exist, create it new
        if force or not os.path.exists(outfile):
            Render(path, rect_id, dpi, outfile)
            if verbose:
                print("├─ Rendered new \"" + outfile + "\"")
            Output.new_renders += 1

        # If PNG exists, compare modify time to that of SVG
        else:
            stat_in = os.stat(path)
            stat_out = os.stat(outfile)

            # If SVG is newer than PNG, replace PNG with updated version
            if stat_in.st_mtime > stat_out.st_mtime:
                Render(path, rect_id, dpi, outfile)
                if verbose:
                    print("├─ Rendered updated \"" + outfile + "\"")
                # print("Rendered updated " + outfile)
                Output.updated_renders += 1

            # If PNG is newer than SVG, leave PNG as is
            else:
                if verbose:
                    print("├─ \"" + outfile + "\" is newer than SVG")
                Output.skipped_renders += 1
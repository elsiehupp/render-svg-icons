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

from .parse_svg import ParseSvg

def render_category(args, category_to_render):

    # If invocation includes a file name, try to process it
    if args.individual_icons:
        file = os.path.join(category_to_render, args.individual_icons + '.svg')

        if os.path.exists(os.path.join(file)):
            print("├─ Rendering from \"" + os.path.join(file) + "\"")
            ParseSvg(file, args, True)
            return True

        else:
            # icon not in this directory, try the next one
            print("├─ Input file \"" + file + "\" does not exist.")
            return False

    # If invocation does not include a file name, process all SVGs in listed sources
    else:
        print("Rendering from path \"" + category_to_render + "\"")
        if not os.path.exists(args.output_path):
            os.mkdir(args.output_path)

        # this is the loop for the files in the given directory
        for file in os.listdir(category_to_render):
            if file[-4:] == '.svg':
                ParseSvg(os.path.join(category_to_render, file), args)
        
        return True




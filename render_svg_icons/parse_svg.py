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

import xml.sax

from .output import Output

class ParseSvg(xml.sax.ContentHandler):
    #
    # ParseSvg() implements an interface for xml.sax.parse()
    #

    ROOT = 0
    SVG = 1
    LAYER = 2
    OTHER = 3
    TEXT = 4

    def __init__(self, path, args, force=False):
        self.args = args
        self.stack = [self.ROOT]
        self.inside = [self.ROOT]
        self.path = path
        self.rects = []
        self.state = self.ROOT
        self.chars = ""
        self.force = force
        self.filter = args.filter

        #
        # xml.sax.parse() uses the various ContentHandler() methods behind the scenes
        #
        xml.sax.parse(open(self.path), self)

    def endDocument(self):
        pass

    def startElement(self, name, attrs):
        if self.inside[-1] == self.ROOT:
            if name == "svg":
                self.stack.append(self.SVG)
                self.inside.append(self.SVG)
                return
        elif self.inside[-1] == self.SVG:
            for attr in attrs.values():
                if attr == 'Baseplate':
                    self.stack.append(self.LAYER)
                    self.inside.append(self.LAYER)
                    self.context = None
                    self.icon_name = None
                    self.rects = []
                    return
        elif self.inside[-1] == self.LAYER:
            for attr in attrs.values():
                if attr == "context":
                    self.stack.append(self.TEXT)
                    self.inside.append(self.TEXT)
                    self.text='context'
                    self.chars = ""
                    return
                if attr == "icon-name":
                    self.stack.append(self.TEXT)
                    self.inside.append(self.TEXT)
                    self.text='icon-name'
                    self.chars = ""
                    return
                if name == "rect":
                    self.rects.append(attrs)
        self.stack.append(self.OTHER)


    def endElement(self, name):
        stacked = self.stack.pop()
        if self.inside[-1] == stacked:
            self.inside.pop()

        if stacked == self.TEXT and self.text is not None:
            assert self.text in ['context', 'icon-name']
            if self.text == 'context':
                self.context = self.chars
            elif self.text == 'icon-name':
                self.icon_name = self.chars
            self.text = None

        elif stacked == self.LAYER:
            assert self.icon_name
            assert self.context

            if self.filter is not None and not self.icon_name in self.filter:
                return

            new_renders = 0
            updated_renders = 0
            skipped_renders = 0

            # Each rect represents an icon size to export
            for rect in self.rects:
                for dpi_factor in self.args.scaling_factors:
                    width = rect['width']
                    # height = rect['height']
                    rect_id = rect['id']
                    dpi = self.args.base_dpi * dpi_factor

                    size_str = "%s" % (width)
                    if dpi_factor != 1:
                        size_str += "@%sx" % dpi_factor

                    Output(
                        self.args.context,
                        rect_id,
                        self.args.output_path,
                        size_str,
                        self.args.icon_name,
                        self.args.path,
                        dpi,
                        self.args.force,
                        self.args.verbose)

            # Print horizontal rule below long list
            if self.args.verbose:
                print("├────────────────────────────────┤")

            # Print summary
            if self.args.individual_icons is None:
                print("")
                print("┌────────────────────────────────┐")
                print("│ Directory: " + self.context)
                print("│ Icon Name: " + self.icon_name)
                print("├────────────────────────────────┤")
                print("├─ Rendered %d new PNGs" % new_renders)
                print("├─ Rendered %d updated PNGs" % updated_renders)
                print("├─ Skipped %d up-to-date PNGs" % skipped_renders)
                print("└────────────────────────────────┘")
                print("")

    def characters(self, chars):
        self.chars += chars.strip()


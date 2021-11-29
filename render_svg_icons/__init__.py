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

import argparse
import os
import sys

from .dependencies import Dependencies
from .render_category import *


def print_help():

    print("")
    print("┌──────────────────────────────────────────────────┐")
    print("│ Render icons from SVG to PNG                     │")
    print("└──────────────────────────────────────────────────┘")
    print("┌──────────────────────────────────────────────────┐")
    print("│ Usage                                            │")
    print("├──────────────────────────────────────────────────┤")
    print("│ $ render_svg_icons                               │")
    print("│       [--help]                                   │")
    print("│       [--base_dpi BASE_DPI]                      │")
    print("│       [--categories [CATEGORIES]]                │")
    print("│       [--filter FILTER]                          │")
    print("│       [--inkscape_path INKSCAPE_PATH]            │")
    print("│       [--individual_icons [INDIVIDUAL_ICONS]]    │")
    print("│       [--optipng_path OPTIPNG_PATH]              │")
    print("│       [--output_path OUTPUT_PATH]                │")
    print("│       [--scaling_factors [SCALING_FACTORS]]      │")
    print("│       [--verbose]                                │")
    print("│                                                  │")
    print("└──────────────────────────────────────────────────┘")
    print("┌──────────────────────────────────────────────────┐")
    print("│ Optional Arguments                               │")
    print("├──────────────────────────────────────────────────┤")
    print("│ --help                                           │")
    print("│                                                  │")
    print("│   Show this help message and exit.               │")
    print("│                                                  │")
    print("│ --base_dpi BASE_DPI                              │")
    print("│                                                  │")
    print("│   dpi to use for rendering (by default 96)       │")
    print("│                                                  │")
    print("│ --categories [CATEGORIES]                        │")
    print("│                                                  │")
    print("│   categories of icons to render (by default all) │")
    print("│                                                  │")
    print("│ --filter FILTER                                  │")
    print("│                                                  │")
    print("│   Inkscape filter to apply while rendering       │")
    print("│   (by default none)                              │")
    print("│                                                  │")
    print("│ --inkscape_path INKSCAPE_PATH                    │")
    print("│                                                  │")
    print("│   path of Inkscape executable                    │")
    print("│   (if the script can't find it)                  │")
    print("│                                                  │")
    print("│ --individual_icons [INDIVIDUAL_ICONS]            │")
    print("│                                                  │")
    print("│   individual icon names (without extensions)     │")
    print("│   to render (by default all)                     │")
    print("│                                                  │")
    print("│ --optipng_path OPTIPNG_PATH                      │")
    print("│                                                  │")
    print("│   path of OptiPNG executable                     │")
    print("│   (if the script can't find it)                  │")
    print("│                                                  │")
    print("│ --output_path OUTPUT_PATH                        │")
    print("│                                                  │")
    print("│   output directory (by default '.')              │")
    print("│                                                  │")
    print("│ --scaling_factors [SCALING_FACTORS]              │")
    print("│                                                  │")
    print("│   scaling factors to render at                   │")
    print("│   (by default [1, 2], e.g. 100% & 200%)          │")
    print("│                                                  │")
    print("│ --verbose                                        │")
    print("│                                                  │")
    print("│   print verbose output to the terminal           │")
    print("│                                                  │")
    print("└──────────────────────────────────────────────────┘")
    print("")
    return


def print_categories():

    print("")
    print("┌────────────────────────────────┐")
    print("│ Icon Categories:               │")
    print("├────────────────────────────────┤")
    print("│ - actions                      │")
    print("│ - apps                         │")
    print("│ - categories                   │")
    print("│ - devices                      │")
    print("│ - emblems                      │")
    print("│ - legacy                       │")
    print("│ - mimetypes                    │")
    print("│ - places                       │")
    print("│ - status                       │")
    print("│ - wip                          │")
    print("└────────────────────────────────┘")
    print("")
    return


def build_parser():

    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument(
        '--categories',
        type=str,
        nargs='?',
        default=(
            "actions",
            "apps",
            "categories",
            "devices",
            "emblems",
            "legacy",
            "mimetypes",
            "places",
            "status",
            "wip",
        ),
        help="categories of icons to render (by default all)"
    )
    parser.add_argument(
        '--base_dpi',
        type=int,
        nargs=1,
        default=96,
        help="dpi to use for rendering (by default 96)"
    )
    parser.add_argument(
        '--filter',
        type=str,
        nargs=1,
        help="Inkscape filter to apply while rendering (by default none)"
    )
    parser.add_argument(
        '--help',
        action='store_true',
        help="show this help message and exit"
    )
    if sys.platform.startswith('linux'):
        parser.add_argument(
            '--inkscape_path',
            type=str,
            nargs=1,
            default = '/usr/bin/inkscape',
            help="path of Inkscape executable (if the script can't find it)"
        )
        parser.add_argument(
            '--optipng_path',
            type=str,
            nargs=1,
            default = '/usr/bin/optipng',
            help="path of OptiPNG executable (if the script can't find it)"
        )
    elif sys.platform.startswith('darwin'):
        parser.add_argument(
            '--inkscape_path',
            type=str,
            nargs=1,
            default = '/Applications/Inkscape.app/Contents/MacOS/inkscape',
            help="path of Inkscape executable (if the script can't find it)"
        )
        parser.add_argument(
            '--optipng_path',
            type=str,
            nargs=1,
            default = '/usr/local/bin/optipng',
            help="path of OptiPNG executable (if the script can't find it)"
        )
    parser.add_argument(
        '--individual_icons',
        type=str,
        nargs='?',
        help="individual icon names (without extensions) to render (by default all)"
    )
    parser.add_argument(
        '--list_categories',
        action='store_true',
        help="list categories of icons to choose from and exit"
    )
    parser.add_argument(
        '--output_path',
        type=str,
        nargs=1,
        default = '.',
        help="output directory (by default '.')"
    )
    parser.add_argument(
        '--scaling_factors',
        type=int,
        nargs='?',
        default=[1, 2],
        help="scaling factors to render at (by default [1, 2])"
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help="print verbose output to the terminal"
    )
    return parser


def do(args):

    if args.list_categories:
        print_categories()
        return None

    if args.help:
        print_help()
        return None

    Dependencies(
        inkscape_path = args.inkscape_path,
        optipng_path = args.optipng_path,
        output_path = args.output_path)

    if args.individual_icons is None:
        print("\nNo arguments provided; processing listed sources:\n")
        for icon_category in args.categories:
            print("-- \"" + os.path.join('.', icon_category) + "\"")
        print("")
    else:
        print("┌────────────────────────────────┐")
        print("│ Rendering from command-line argument \"" + args.individual_icons + "\"")
        print("├────────────────────────────────┤")

    class Result:
        def __init__(self, args):
            self.directory = ""
            self.named = args.individual_icons

    result = Result(args)

    for source in args.categories:
        if os.path.exists(os.path.join('.', source)):
            SRC = os.path.join('.', source)
            #
            # render_category() is the main function call
            #
            if render_category(args, SRC):
                result.directory = source
        else:
            print("Source path \"" + os.path.join('.', source) + "\" does not exist.")
    if args.individual_icons is not None:
        print("└────────────────────────────────┘")

    return result


def print_result(result):

    if result is None: return

    if result.directory != "" and result.named is not None:
        print("\nSuccessfully processed \"" + result.named + "\" in \"" + result.directory + "\".\n")
    elif result.directory == "" and result.named is not None:
        print("\nFailed to process \"" + result.named + "\" in " + result.directory + ".\n")
    elif result.directory != "":
        print("Successfully processed listed sources.\n")
    elif result.directory == "":
        print("Failed to process listed sources.\n")
    else:
        raise Exception("Conditional statement falls through.")
    return


def main():

    # This is the main function
    print_result(do(build_parser().parse_args()))
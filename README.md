`render-svg-icons` is a python script for rendering SVG icons to PNG icons in various sizes. While it runs on both Linux and macOS, it currently uses a specific SVG template and a folder structure based on [the XDG Icon Theme Specification](https://specifications.freedesktop.org/icon-theme-spec/latest/).

# Provenance

I've come across the progenitor of this script in multiple places. It seems to have originated with GNOME, but it's not entirely clear.

# Development Status

`render-svg-icons` _should_ basically work for its original purpose of rendering XDG icon themes. I plan to continue adapting the code to make it easier to use and to allow for more flexible use cases in the future.

While I plan to leave the command-line interface more or less intact, it and the implementation thereof shouldn't be considered stable at the moment. If you plan to call `render-svg-icons` as a dependency, you should specify an exact version you know to work for your purposes.

# Installation

For day-to-day use, you should install `render-svg-icons` from PyPI:

```bash
$ pip install render-svg-icons
```

For development purposes, you can build and install `render-svg-icons` from the cloned repository using [Poetry](https://python-poetry.org/).

To install Poetry, run:

```bash
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Then, from the `render-svg-icons` cloned repository, run:

```bash
$ poetry build
$ pip install --force-reinstall dist/*.whl
```

This will install the repository code in the same manner as the PyPI version. (The `--force-reinstall` causes it to overwrite any other installed version.)

To uninstall either version of `render-svg-icons`, run:

```bash
$ pip uninstall render-svg-icons
```

# Dependencies

`render-svg-icons` requires both [Inkscape](https://inkscape.org/) and [OptiPNG](http://optipng.sourceforge.net/).

## Linux

To install Inkscape and OptiPNG on, e.g., Debian, Ubuntu, etc.:

```bash
$ sudo apt install inkscape optipng
```

(For Fedora, Arch, etc., I'm sure you know what you're doing.)

## macOS

To install Inkscape and OptiPNG on macOS, first install [Homebrew](https://brew.sh/) if you haven't already:

```bash
% /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then use Homebrew to install Inkscape and OptiPNG:

```
% brew install inkscape optipng
```

You can probably use other installation methods, but you may need to specify the executable path if it's different from the one used by Homebrew.

## Other Platforms

`render-svg-icons` isn't currently compatible with platforms other than Linux and macOS. If you'd like to use this on another platform, please [open an issue](https://github.com/elsiehupp/render-svg-icons/issues/new) or [a pull request](https://github.com/elsiehupp/render-svg-icons/compare).

# Usage

After installation:

```bash
$ render_svg_icons --help

┌──────────────────────────────────────────────────┐
│ Render icons from SVG to PNG                     │
└──────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────┐
│ Usage                                            │
├──────────────────────────────────────────────────┤
│ $ render_svg_icons                               │
│       [--help]                                   │
│       [--base_dpi BASE_DPI]                      │
│       [--categories [CATEGORIES]]                │
│       [--filter FILTER]                          │
│       [--inkscape_path INKSCAPE_PATH]            │
│       [--individual_icons [INDIVIDUAL_ICONS]]    │
│       [--optipng_path OPTIPNG_PATH]              │
│       [--output_path OUTPUT_PATH]                │
│       [--scaling_factors [SCALING_FACTORS]]      │
│       [--verbose]                                │
│                                                  │
└──────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────┐
│ Optional Arguments                               │
├──────────────────────────────────────────────────┤
│ --help                                           │
│                                                  │
│   Show this help message and exit.               │
│                                                  │
│ --base_dpi BASE_DPI                              │
│                                                  │
│   dpi to use for rendering (by default 96)       │
│                                                  │
│ --categories [CATEGORIES]                        │
│                                                  │
│   categories of icons to render (by default all) │
│                                                  │
│ --filter FILTER                                  │
│                                                  │
│   Inkscape filter to apply while rendering       │
│   (by default none)                              │
│                                                  │
│ --inkscape_path INKSCAPE_PATH                    │
│                                                  │
│   path of Inkscape executable                    │
│   (if the script can't find it)                  │
│                                                  │
│ --individual_icons [INDIVIDUAL_ICONS]            │
│                                                  │
│   individual icon names (without extensions)     │
│   to render (by default all)                     │
│                                                  │
│ --optipng_path OPTIPNG_PATH                      │
│                                                  │
│   path of OptiPNG executable                     │
│   (if the script can't find it)                  │
│                                                  │
│ --output_path OUTPUT_PATH                        │
│                                                  │
│   output directory (by default '.')              │
│                                                  │
│ --scaling_factors [SCALING_FACTORS]              │
│                                                  │
│   scaling factors to render at                   │
│   (by default [1, 2], e.g. 100% & 200%)          │
│                                                  │
│ --verbose                                        │
│                                                  │
│   print verbose output to the terminal           │
│                                                  │
└──────────────────────────────────────────────────┘
```

# License

`render-svg-icons` is published under the GPLv3 or later (i.e. you can use it for proprietary purposes via the command line, but you can only link to it from other GPL code).
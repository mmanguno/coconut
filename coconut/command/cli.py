#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------------------------------------------
# INFO:
#-----------------------------------------------------------------------------------------------------------------------

"""
Authors: Evan Hubinger
License: Apache 2.0
Description: Defines arguments for the Coconut CLI.
"""

#-----------------------------------------------------------------------------------------------------------------------
# IMPORTS:
#-----------------------------------------------------------------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

from coconut.root import *  # NOQA

import argparse

from coconut.constants import (
    documentation_url,
    version_long,
    default_recursion_limit,
)

#-----------------------------------------------------------------------------------------------------------------------
# MAIN:
#-----------------------------------------------------------------------------------------------------------------------

arguments = argparse.ArgumentParser(
    prog="coconut",
    description=documentation_url)

arguments.add_argument(
    "source",
    metavar="source",
    type=str,
    nargs="?",
    help="path to the Coconut file/folder to compile")

arguments.add_argument(
    "dest",
    metavar="dest",
    type=str,
    nargs="?",
    help="destination directory for compiled files (defaults to the source directory)")

arguments.add_argument(
    "-v", "--version",
    action="version",
    version=version_long,
    help="print Coconut and Python version information")

arguments.add_argument(
    "-t", "--target",
    metavar="version",
    type=str,
    help="specify target Python version (defaults to universal)")

arguments.add_argument(
    "-s", "--strict",
    action="store_true",
    help="enforce code cleanliness standards")

arguments.add_argument(
    "-l", "--line-numbers", "--linenumbers",
    action="store_true",
    help="add line number comments for ease of debugging")

arguments.add_argument(
    "-k", "--keep-lines", "--keeplines",
    action="store_true",
    help="include source code in comments for ease of debugging")

arguments.add_argument(
    "-p", "--package",
    action="store_true",
    help="compile source as part of a package (defaults to only if source is a directory)")

arguments.add_argument(
    "-a", "--standalone",
    action="store_true",
    help="compile source as standalone files (defaults to only if source is a single file)")

arguments.add_argument(
    "-w", "--watch",
    action="store_true",
    help="watch a directory and recompile on changes (requires watchdog)")

arguments.add_argument(
    "-d", "--display",
    action="store_true",
    help="print compiled Python")

arguments.add_argument(
    "-r", "--run",
    action="store_true",
    help="run compiled Python (often used with --nowrite)")

arguments.add_argument(
    "-n", "--nowrite",
    action="store_true",
    help="disable writing compiled Python")

arguments.add_argument(
    "-m", "--minify",
    action="store_true",
    help="compress compiled Python")

arguments.add_argument(
    "-i", "--interact",
    action="store_true",
    help="force the interpreter to start (otherwise starts if no other command is given)")

arguments.add_argument(
    "-q", "--quiet",
    action="store_true",
    help="suppress all informational output (combine with --display to write runnable code to stdout)")

arguments.add_argument(
    "-f", "--force",
    action="store_true",
    help="force overwriting of compiled Python (otherwise only overwrites when source code or compilation parameters change)")

arguments.add_argument(
    "-c", "--code",
    metavar="code",
    type=str,
    help="run a line of Coconut passed in as a string (can also be passed into stdin)")

arguments.add_argument(
    "-j", "--jobs",
    metavar="processes",
    type=str,
    help="number of additional processes to use (defaults to 0) (pass 'sys' to use machine default)")

arguments.add_argument(
    "--jupyter", "--ipython",
    type=str,
    nargs=argparse.REMAINDER,
    help="run Jupyter/IPython with Coconut as the kernel (remaining args passed to Jupyter)")

arguments.add_argument(
    "--tutorial",
    action="store_true",
    help="open the Coconut tutorial in the default web browser")

arguments.add_argument(
    "--documentation",
    action="store_true",
    help="open the Coconut documentation in the default web browser")

arguments.add_argument(
    "--style",
    metavar="name",
    type=str,
    help="pygments syntax highlighting style (or 'none' to disable)")

arguments.add_argument(
    "--recursion-limit", "--recursionlimit",
    metavar="limit",
    type=int,
    help="set maximum recursion depth in compiler (defaults to " + str(default_recursion_limit) + ")")

arguments.add_argument(
    "--verbose",
    action="store_true",
    help="print verbose debug output")

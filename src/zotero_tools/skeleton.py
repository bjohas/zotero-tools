#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         fibonacci = zotero_tools.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""

import argparse
import sys
import logging
import json

from pyzotero import zotero

from zotero_tools import __version__

__author__ = "tadaley"
__copyright__ = "tadaley"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Dump records from a Zotero library")
    parser.add_argument(
        '--api_key',
        required=True,
        help='Zotero API key')
    parser.add_argument(
        '--library_id',
        required=True,
        type=int,
        help="Zotero library numeric ID")
    parser.add_argument(
        '--library_type',
        required=True,
        choices=('user', 'group'),
        help="Zotero library type [user|group]")
    parser.add_argument(
        '--tag',
        help='Filter by tag')
    parser.add_argument(
        '-v',
        '--verbose',
        dest="loglevel",
        help="set loglevel to INFO",
        action='store_const',
        const=logging.INFO)
    parser.add_argument(
        '-vv',
        '--very-verbose',
        dest="loglevel",
        help="set loglevel to DEBUG",
        action='store_const',
        const=logging.DEBUG)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def zotero_get(api_key, library_id, library_type, tag=None):
    zot = zotero.Zotero(library_id, library_type, api_key)
    items = zot.everything(zot.items(tag=tag))
    for item in items:
        print(json.dumps(items))


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("zotero-get: %s", args)
    zotero_get(args.api_key, args.library_id, args.library_type, args.tag)
    _logger.info("Finished")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()

#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Michael Trepanier"

import sys
import signal
import time
import os
from datetime import datetime
import logging
import argparse

# initialize
polling_interval = 1
extension = ""
polling_dir = "."
magic_text = ""
exit_flag = False
files = {}
prog_start_time = datetime.now()

# create logger
logger = logging.getLogger('deerz')
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def create_parser(args):
    global polling_interval
    global extension
    global polling_dir
    global magic_text
    # Your code here
    # - An argument that controls the polling interval (instead of hard-coding it)
    # - An argument that specifics the "magic text" to search for
    # - An argument that filters what kind of file extension to search within (i.e., `.txt`, `.log`)
    # - An argument to specify the directory to watch (*this directory may not yet exist!*)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--interval', help='polling interval, default is one second')
    parser.add_argument('directory', help='directoryto search')
    parser.add_argument('ext', help='magic text')
    parser.add_argument('magictext', help='magic text to search for')
    #
    ns = parser.parse_args(args)
    logger.info('args: '+str(ns))

    if (ns.interval != None):
        polling_interval = ns.interval
    if (ns.directory != None):
        polling_dir = ns.directory
    if (ns.ext != None):
        extension = ns.ext
    if (ns.magictext != None):
        magic_text = ns.magictext
    return None


def search_for_magic(filename, start_line, magic_string):
    # Your code here
    global files

    with open(filename) as f:
        if (start_line > 1):
            for i in range(start_line-1):
                next(f)
        for line in f:
            if magic_string in line:
                logger.warning('Found '+magic_string+' in file ' +
                               filename+' at line '+str(start_line))
            start_line += 1

    files[filename] = start_line
    return


def watch_directory(path, magic_string, extension, interval):
    # Your code here
    global files
    if (os.path.exists(path)):
        for file in os.listdir(path):
            if file.endswith(extension):
                filename = os.path.join(path, file)
                if filename in files:
                    start_line = files[filename]
                else:
                    start_line = 1
                logger.info('checking file '+filename +
                            ' starting at line '+str(start_line))
                search_for_magic(filename, start_line, magic_string)
    else:
        logger.warning("directory "+path+" does not exist")
    return


def signal_handler(sig_num, frame):
    global exit_flag
    """
    This is a handler for SIGTERM and SIGINT. Other signals can be mapped here as well (SIGHUP?)
    Basically, it just sets a global flag, and main() will exit its loop if the signal is trapped.
    :param sig_num: The integer signal number that was trapped from the OS.
    :param frame: Not used
    :return None
    """
    # log the associated signal name
    logger.warning('Received ' + signal.Signals(sig_num).name)
    exit_flag = True
    return None


def main(args):
    logger.info("deerz starting...")
    # Hook into these two signals from the OS
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now my signal_handler will get called if OS sends
    # either of these to my process.
    create_parser(args)

    while not exit_flag:
        try:
            # call my directory watching function
            watch_directory(polling_dir, magic_text,
                            extension, polling_interval)

        except Exception as e:
            # This is an UNHANDLED exception
            # Log an ERROR level message here
            logger.exception("Exception: {}".format(e.message))

        # put a sleep inside my while loop so I don't peg the cpu usage at 100%
        time.sleep(polling_interval)

    # final exit point happens here
    # Log a message that we are shutting down
    logger.info('Exiting Deerz now...')
    logger.info('Program run time '+str(datetime.now() - prog_start_time))
    # Include the overall uptime since program start


if __name__ == '__main__':
    main(sys.argv[1:])

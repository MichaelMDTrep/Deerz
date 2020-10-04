#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Michael Trepanier"
# function that is going to be reserved for callback it gets invoked by predefined functions

import signal
import time
import sys
import os
import logging

logging.basicConfig(
    format=('%(asctime)s.%(msecs)03d %(name)-12s \
            %(levelname)-8s [%(threadName)-12s] %(message)s',
    datefmt == '%Y-%m-%d %H:%M:%S'
)
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
exit_flag=False


def search_for_magic(filename, start_line, magic_string):

    return


def watch_directory(path, magic_string, extension, interval):
    # Your code here
    return


def create_parser():
    # Your code here
    return


def signal_handler(sig_num, frame):
    """  This is a handler for SIGTERM and SIGINT. Other signals can be mapped here as well (SIGHUP?)
      Basically, it just sets a global flag, and main() will exit its loop if the signal is trapped.
      :param sig_num: The integer signal number that was trapped from the OS.
      :param frame: Not used
      :return None
      """
    global exit_flag
    print("Got a signal!", signal.signals(sig_num).name)
    exit_flag=True
    # logger.warn('Received ' + signal.Signals(sig_num).name)

    return


interval=1.0


def main(args):
    # counter = 1
    # while True:
    #     file_list = os.listdir()
    #     print(file_list)
    #     for f in file_list:
    #         if f.endswith('.log'):
    #             # with open(f, "r" as handle):
    #             if "HAXOR" in handle.read():
    #                 print("WARNING: Hacker has logged in")
    #                 print("I found a log!")
    # time.sleep(interval)
    # logger.debug("A debug message for the logs!")

    if not counter % 5:
        # other.func()
        counter += 1
    logger.warning('This is information')
 # Hook into these two signals from the OS
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now my signal_handler will get called if OS sends
    # either of these to my process.
    global exit_flag
    while not exit_flag:
        try:
            # my_list = [1, 2]
            # x = my_list[3]
            print("Tick...")
            time.sleep(2)
            print("Tock...")
            time.sleep(2)
        except KeyboardInterrupt:
            print('I do not enjoy being interrupted!')
            break
        else:
            print('I am else')
        finally:
            print("I am inevitable")
            print("I think you mean [-1]")
            # x = my_list[-1]
    #     except Exception:
    # print('All done.')
    #    try:
    # call my directory watching function
    # pass
    # except Exception as e:
    # This is an UNHANDLED exception
    # Log an ERROR level message here
    # pass

    # put a sleep inside my while loop so I don't peg the cpu usage at 100%
    # time.sleep(polling_interval)

    # final exit point happens here
    # Log a message that we are shutting down
    # Include the overall uptime since program start    return


if __name__ == '__main__':
    for item in range(10):
        logger=my_custom_logger(f"Logger{item}")
        logger.debug(item)
    main(sys.argv[1:])

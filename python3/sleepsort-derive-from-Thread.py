#!/usr/bin/env python3

"""
Implemented that sub-classes threading.Thread
"""

import sys
import threading
import time


class DelayedEcho(threading.Thread):

    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        time.sleep(self.n)
        print(self.n)


def sleepsort(numbers):
    # Guard against non-integer input by converting to int upfront.
    numbers = [int(n) for n in numbers]
    echoers = []
    for n in numbers:
        echoer = DelayedEcho(n)
        echoer.start()
        echoers.append(echoer)

    for echoer in echoers:
        echoer.join()


if __name__ == '__main__':
    sleepsort(sys.argv[1:])

#!/usr/bin/env python3

"""
Implemented using Thread objects that are 'joined' at the end.
"""

import sys
import threading
import time


def sleepsort(numbers):
    # Guard against non-integer input by converting to int upfront.
    numbers = [int(n) for n in numbers]

    def delayed_echo(n):
        time.sleep(n)
        print(n)

    threads = []
    for n in numbers:
        thread = threading.Thread(target=delayed_echo, args=(n,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    sleepsort(sys.argv[1:])

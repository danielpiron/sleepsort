#!/usr/bin/env python3

"""
Implemented using Thread objects that are 'joined' at the end.
"""

import sys
import threading
import time

if __name__ == '__main__':

    numbers = sys.argv[1:]
    def delayed_echo(n):
        time.sleep(n)
        print(n)

    threads = []
    for n in numbers:
        thread = threading.Thread(target=delayed_echo, args=(int(n),))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

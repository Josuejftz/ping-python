import time
import multiprocessing
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ping3  # noqa: linter (pycodestyle) should not lint this line.


print("ping3=", ping3.__version__)
# ping3.DEBUG = True
HOSTS = ['192.168.50.51',
'192.168.50.242',
'192.168.50.241',
'192.168.50.100',
'192.168.50.60',
'192.168.50.30',
'192.168.50.24',
'192.168.50.23',
'192.168.50.20',
'192.168.50.10',
'192.168.50.5',
'192.168.50.1',]

def ping_in_thread_or_process(host):
    while True:
        delay = ping3.ping(host, unit='ms')
        time.sleep(30)
        print(host, delay)


def standard_delay():
    for h in HOSTS:
        print('Standard Delay:', h, ping3.ping(h, unit='ms'))


def multi_processing_ping():
    for h in HOSTS:
        p = multiprocessing.Process(target=ping_in_thread_or_process, args=(h,))
        p.start()


if __name__ == '__main__':
    standard_delay()
    multi_processing_ping()
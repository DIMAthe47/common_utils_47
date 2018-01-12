from contextlib import contextmanager
from timeit import default_timer

import time


@contextmanager
def elapsed_timer():
    start = default_timer()
    elapser = lambda: default_timer() - start
    yield lambda: elapser()
    end = default_timer()
    elapser = lambda: end - start


if __name__ == '__main__':
    with elapsed_timer() as elapsed:
        time.sleep(1)
        print(elapsed())
        time.sleep(2)
        print(elapsed())
        time.sleep(3)

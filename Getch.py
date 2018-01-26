import time

class _Getch:

    """Gets a single character from standard input.  Does not echo to the screen. 
    Can be called with specified timeout."""

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self, timeout=-1): return self.impl(timeout)


class _GetchUnix:

    def __init__(self):
        import tty
        import sys

    def __call__(self, timeout=-1):
        import sys
        import tty
        import termios
        import select
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            if timeout != -1:
                i, o, e = select.select([sys.stdin], [], [], timeout)
                if (i):
                    ch = sys.stdin.read(1)
                else:
                    ch = None
            else:
                ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:

    def __init__(self):
        import msvcrt

    def __call__(self, timeout=-1):
        import msvcrt
        if timeout==-1:
            return chr(ord(msvcrt.getch()))
        else:
            start_time=time.time()
            while True:
                if msvcrt.kbhit():
                    return chr(ord(msvcrt.getch()))
                    break
                elif time.time() - start_time > timeout:
                    return None
                    break


getch = _Getch()

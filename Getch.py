class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen. (Added timemout option, if you call getch(timeout) ~ d0ku)
Credits: tehvan from StackOverflow for initial class"""

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
        return msvcrt.getch()


getch = _Getch()

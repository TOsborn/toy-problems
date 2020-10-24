from recursion_tools import memoize
import pytest

@pytest.mark.timeout(1)
def test_memoize():
    @memoize
    def fib(n):
        if n in (0, 1):
            return n

        return fib(n-1) + fib(n-2)

    fib(100)

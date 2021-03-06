from functools import lru_cache


@lru_cache
def rec_feb(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

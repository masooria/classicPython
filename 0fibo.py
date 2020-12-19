from typing import Dict, Generator
import time
from functools import lru_cache


def fibo(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


# start_time = time.time()
# print(fibo(35))
# end_time = time.time()
# print(end_time - start_time)


memo: Dict[int, int] = {0: 0, 1: 1}


def memo_fibo(n: int) -> int:
    if n not in memo:
        memo[n] = memo_fibo(n - 1) + memo_fibo(n - 2)
    return memo[n]


# start_time = time.time()
# print(memo_fibo(499))
# end_time = time.time()
# print(end_time - start_time)


# Using lru cache, built-in decorator for memoizing any function automagically
@lru_cache(maxsize=None)
def fibo_lru(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_lru(n - 1) + fibo_lru(n - 2)


# start_time = time.time()
# print(fibo_lru(499))
# end_time = time.time()
# print(end_time - start_time)


def iter_fibo(n: int) -> int:
    if n == 0:
        return n
    last: int = 0
    nxt: int = 1
    for _ in range(1, n):
        last, nxt = nxt, last + nxt
    return nxt


# start_time = time.time()
# print(iter_fibo(499))
# end_time = time.time()
# print(end_time - start_time)


def gen_fibo(n: int):
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    nxt: int = 1
    for _ in range(1, n):
        last, nxt = nxt, last + nxt
        yield nxt


for i in gen_fibo(50):
    print(i)

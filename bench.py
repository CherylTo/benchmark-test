import pytest

def add():
    a = 1
    b = 2
    return a+b

def test_bench(benchmark):
    res = benchmark(add)
    assert res == 3

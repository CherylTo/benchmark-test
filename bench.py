import pytest
import json
import time

def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

def test_bench():
    sum = add(1, 2)
    product = multiply(2, 3)
    ts = str(int(time.time()))
    data = {
        "time": time.time
        "add": [{"a": 1, "b": 2, "add": sum}],
	    "multiply": [{"a": 2, "b": 3, "multiply": product}]
    }
    file_name = ts+'_test.json'
    with open(file_name, 'w') as file:
        json.dump(data, file)

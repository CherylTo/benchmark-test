import pytest
import json

def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

def test_bench():
    sum = add(1, 2)
    product = multiply(2, 3)
    data = {
        "add": [{"a": 1, "b": 2, "add": sum}],
	"multiply": [{"a": 2, "b": 3, "multiply": product}]
    }
    with open('test.json', 'w') as file:
        json.dump(data, file)

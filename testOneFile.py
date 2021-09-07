import pytest


def oneTwo(a, b):
    return a+b


@pytest.mark.one
def testOneTwo():
    assert oneTwo(10, 11) == 21


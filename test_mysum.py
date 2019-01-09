#!/usr/bin/python

from mysum import mysum
import pytest

#def test_sum_integers():
#  assert mysum([0,1,2,3,4]) == 10

#def test_sum_nothing():
#  assert mysum([]) == 0

#def test_sum_floats():
#  assert mysum([0.1,1.2,2.3,3.4,4.5]) == 11.5

#def test_one_and_one_are_three():
#  assert mysum([1,1]) == 3

@pytest.mark.parametrize('numbers,output', [
    ([], 0),
    ([10, 20, 30], 60),
    ([0.1, 1.2, 2.3, 3.4, 4.5], 11.5)])

def test_mysum(numbers, output):
  assert mysum(numbers) == output

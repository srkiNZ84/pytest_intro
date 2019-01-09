#!/usr/bin/python

from double import double
from io import StringIO
import pytest

number_inputs = StringIO(u'1234\n')

def test_double(monkeypatch):
  monkeypatch.setattr('sys.stdin', number_inputs)
  assert double() == 2468

str_inputs = StringIO(u'abcd\n')
def test_double_str(monkeypatch):
  with pytest.raises(NameError) as e:
    monkeypatch.setattr('sys.stdin', str_inputs)
    result = double()
  assert str(e.value) == "name 'abcd' is not defined"

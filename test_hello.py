#!/usr/bin/python

from hello import hello
import pytest

def test_hello(capsys):
  hello('world')
  captured_stdout, captured_stderr = capsys.readouterr()
  assert captured_stdout.strip() == 'Hello, world!'

import pytest
from hello import greet, main

def test_greet():
    assert greet("Rumi") == "Hello, Rumi!"

def test_main_prints_greeting(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda prompt="": "Alice")
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, Alice!\n"
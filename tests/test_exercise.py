import pytest
from src.exercise import main

def test_exercise(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == '120\n'

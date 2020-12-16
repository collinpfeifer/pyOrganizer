import organizer
import pytest

def move_test(capsys):
    result = organizer.run()
    out, err = capsys.readouterr()
    assert out.startswith("Moved folder created")

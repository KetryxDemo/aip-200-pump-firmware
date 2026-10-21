import pytest
from aip.dosing import program_rate, to_ml_per_hour


def test_ml_h():
    assert to_ml_per_hour("morphine", "ml_h", 4) == 4


def test_mg_h():
    assert to_ml_per_hour("hydromorphone", "mg_h", 1.0) == 5.0


def test_unsupported_mode():
    with pytest.raises(ValueError):
        to_ml_per_hour("morphine", "furlongs", 1)


def test_needs_confirmation():
    assert program_rate("morphine", "mg_h", 2)["needs_confirmation"]

from aip.drug_library import LimitResult, check_rate


def test_limits():
    assert check_rate("morphine", 5) == LimitResult.OK
    assert check_rate("morphine", 12) == LimitResult.SOFT
    assert check_rate("morphine", 20) == LimitResult.HARD

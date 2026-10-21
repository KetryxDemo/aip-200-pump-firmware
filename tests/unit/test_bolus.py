from aip.bolus import BolusController


def test_lockout():
    b = BolusController("morphine", 1.0, lockout_s=600)
    assert b.request(0)
    assert not b.request(300)
    assert b.request(601)

from aip.pump import Pump


def test_interlock():
    p = Pump()
    assert not p.start()
    p.set_latch(True)
    assert p.start()
    p.set_latch(False)
    assert not p.running and p.clamp_engaged

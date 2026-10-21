from aip.alarms import Alarm


def test_silence_cap():
    a = Alarm("occlusion")
    assert a.silence(0, 3600) == 120
    assert a.audible(121)

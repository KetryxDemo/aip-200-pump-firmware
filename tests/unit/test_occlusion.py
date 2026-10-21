from aip.occlusion import OcclusionDetector, threshold_kpa


def seconds_to_alarm(rate):
    d, p = OcclusionDetector(rate), 0.0
    for t in range(1, 600):
        p += 2.0  # pressure rises 2 kPa/s behind a full occlusion
        if d.update(p):
            return t
    return None


def test_alarm_time():
    for rate in (1, 25, 500):
        t = seconds_to_alarm(rate)
        assert t is not None and t <= 120, (rate, t)


def test_transient_rejected():
    d = OcclusionDetector(5)
    spike = threshold_kpa(5) * 3
    fired = [d.update(spike if t < 3 else 10.0) for t in range(30)]
    assert not any(fired)

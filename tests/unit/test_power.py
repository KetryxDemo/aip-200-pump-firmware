from aip.power import power_alarm


def test_thresholds():
    assert power_alarm(1000, 10) is None
    assert power_alarm(40, 100) == "low_medium"
    assert power_alarm(5, 100) == "depleted_high"

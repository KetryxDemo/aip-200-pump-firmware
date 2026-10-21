from aip.bolus import BolusController
from aip.remote import RemoteBolusService


def svc():
    s = RemoteBolusService(BolusController("morphine", 1.0, lockout_s=600))
    s.pair("phone-1")
    return s


def test_paired_bolus():
    assert svc().on_write({"cmd": "bolus", "seq": 1, "pairing_id": "phone-1"}, 0)


def test_unpaired_rejected():
    assert not svc().on_write({"cmd": "bolus", "seq": 1, "pairing_id": "other"}, 0)


def test_duplicate_seq_dropped():
    s = svc()
    s.on_write({"cmd": "bolus", "seq": 1, "pairing_id": "phone-1"}, 0)
    assert not s.on_write({"cmd": "bolus", "seq": 1, "pairing_id": "phone-1"}, 900)

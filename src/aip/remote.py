"""Companion app remote bolus over Bluetooth Low Energy.

A paired phone app can request a patient bolus. Commands arrive as BLE
GATT writes: {"cmd": "bolus", "seq": <int>, "pairing_id": <str>}.
The pump checks the pairing, drops repeated sequence numbers, then hands the
request to the existing bolus controller (lockout still applies).
"""
from .bolus import BolusController
from .event_log import log


class RemoteBolusService:
    def __init__(self, controller: BolusController):
        self.controller = controller
        self.paired_ids = set()
        self._last_seq = {}

    def pair(self, pairing_id: str):
        self.paired_ids.add(pairing_id)
        log("remote_paired", pairing_id=pairing_id)

    def on_write(self, message: dict, now_s: float) -> bool:
        if message.get("cmd") != "bolus":
            return False
        pid = message.get("pairing_id")
        if pid not in self.paired_ids:
            log("remote_rejected_unpaired", pairing_id=pid)
            return False
        seq = int(message.get("seq", -1))
        if seq <= self._last_seq.get(pid, -1):
            return False  # duplicate or replayed packet
        self._last_seq[pid] = seq
        return self.controller.request(now_s, source="companion_app")

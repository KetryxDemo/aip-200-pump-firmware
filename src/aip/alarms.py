"""Alarm priority, annunciation and silence (SPEC-ALM-01)."""
MIN_VOLUME_DBA = 65
MAX_SILENCE_S = 120
PRIORITY = {"occlusion": "high", "depleted_high": "high", "low_medium": "medium", "hard_limit": "high"}


class Alarm:
    def __init__(self, kind: str):
        self.kind, self.priority = kind, PRIORITY.get(kind, "high")
        self.silenced_until = None

    def silence(self, now_s: float, requested_s: float) -> float:
        self.silenced_until = now_s + min(requested_s, MAX_SILENCE_S)
        return self.silenced_until

    def audible(self, now_s: float) -> bool:
        return self.silenced_until is None or now_s >= self.silenced_until

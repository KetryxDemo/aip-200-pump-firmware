"""Patient bolus with lockout (SPEC-BOL-01). Requests come from the pump keypad."""
from .drug_library import LIBRARY
from .event_log import log


class BolusController:
    def __init__(self, drug: str, bolus_ml: float, lockout_s: int):
        if bolus_ml > LIBRARY[drug].max_bolus_ml:
            raise ValueError("bolus exceeds drug library maximum")
        self.drug, self.bolus_ml, self.lockout_s = drug, bolus_ml, lockout_s
        self._last_bolus_t = None

    def request(self, now_s: float, source: str = "keypad") -> bool:
        if self._last_bolus_t is not None and now_s - self._last_bolus_t < self.lockout_s:
            log("bolus_refused_lockout", source=source)
            return False
        self._last_bolus_t = now_s
        log("bolus_delivered", ml=self.bolus_ml, source=source)
        return True

"""Downstream occlusion detection (SPEC-OCC-01).

Line pressure is sampled at 1 Hz. A moving average over FILTER_WINDOW samples
is compared against a threshold that scales with the programmed rate. An alarm
is raised only after the filtered pressure stays above threshold for
PERSISTENCE_S seconds, which rejects transients from patient movement.
"""
from collections import deque

FILTER_WINDOW = 5          # samples (1 Hz)
PERSISTENCE_S = 10         # seconds above threshold before alarm
BASE_THRESHOLD_KPA = 40.0  # at 1 mL/h
RATE_GAIN_KPA = 0.12       # added per mL/h


def threshold_kpa(rate_ml_h: float) -> float:
    return BASE_THRESHOLD_KPA + RATE_GAIN_KPA * rate_ml_h


class OcclusionDetector:
    def __init__(self, rate_ml_h: float):
        self.rate_ml_h = rate_ml_h
        self._samples = deque(maxlen=FILTER_WINDOW)
        self._above_s = 0

    def filtered(self) -> float:
        return sum(self._samples) / len(self._samples) if self._samples else 0.0

    def update(self, pressure_kpa: float) -> bool:
        """Feed one 1 Hz sample. Returns True when the occlusion alarm should fire."""
        self._samples.append(pressure_kpa)
        if self.filtered() > threshold_kpa(self.rate_ml_h):
            self._above_s += 1
        else:
            self._above_s = 0
        return self._above_s >= PERSISTENCE_S

"""Battery run-time estimate and power alarms (SPEC-PWR-01)."""
LOW_BATTERY_MIN = 30
DEPLETED_MIN = 5


def runtime_min(capacity_mah: float, draw_ma: float) -> float:
    return 60.0 * capacity_mah / draw_ma if draw_ma > 0 else float("inf")


def power_alarm(capacity_mah: float, draw_ma: float):
    t = runtime_min(capacity_mah, draw_ma)
    if t <= DEPLETED_MIN:
        return "depleted_high"
    if t <= LOW_BATTERY_MIN:
        return "low_medium"
    return None

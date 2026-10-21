"""Drug library hard and soft limits (SPEC-LIB-01)."""
from dataclasses import dataclass


@dataclass(frozen=True)
class DrugEntry:
    name: str
    concentration_mg_ml: float
    soft_max_ml_h: float
    hard_max_ml_h: float
    max_bolus_ml: float


LIBRARY = {
    "morphine": DrugEntry("morphine", 1.0, 10.0, 15.0, 2.0),
    "hydromorphone": DrugEntry("hydromorphone", 0.2, 5.0, 8.0, 1.0),
    "saline": DrugEntry("saline", 0.0, 250.0, 500.0, 0.0),
    "dopamine": DrugEntry("dopamine", 1.6, 30.0, 45.0, 0.0),
}


class LimitResult:
    OK = "ok"
    SOFT = "soft_limit_confirm"
    HARD = "hard_limit_reject"


def check_rate(drug: str, rate_ml_h: float) -> str:
    entry = LIBRARY[drug]
    if rate_ml_h > entry.hard_max_ml_h:
        return LimitResult.HARD
    if rate_ml_h > entry.soft_max_ml_h:
        return LimitResult.SOFT
    return LimitResult.OK

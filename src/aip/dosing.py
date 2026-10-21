"""Dose-to-rate conversion (SPEC-DOSE-01).

Supported dosing modes: mL/h (volume) and mg/h (mass). The computed mL/h
rate is always shown to the clinician for confirmation before delivery starts.
"""
from .drug_library import LIBRARY, check_rate

MODES = ("ml_h", "mg_h")


def to_ml_per_hour(drug: str, mode: str, value: float) -> float:
    if mode not in MODES:
        raise ValueError(f"unsupported dosing mode: {mode}")
    if mode == "ml_h":
        return round(value, 2)
    conc = LIBRARY[drug].concentration_mg_ml
    if conc <= 0:
        raise ValueError("mass-based dosing needs a concentration")
    return round(value / conc, 2)


def program_rate(drug: str, mode: str, value: float) -> dict:
    rate = to_ml_per_hour(drug, mode, value)
    return {"rate_ml_h": rate, "limit": check_rate(drug, rate), "needs_confirmation": True}

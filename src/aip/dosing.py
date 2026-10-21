"""Dose-to-rate conversion (SPEC-DOSE-01).

Supported dosing modes: mL/h (volume), mg/h (mass) and mcg/kg/min
(weight-based, for titrated drugs). The computed mL/h
rate is always shown to the clinician for confirmation before delivery starts.
"""
from .drug_library import LIBRARY, check_rate

MODES = ("ml_h", "mg_h", "mcg_kg_min")
MAX_WEIGHT_KG = 250.0


def to_ml_per_hour(drug: str, mode: str, value: float, weight_kg: float = None) -> float:
    if mode not in MODES:
        raise ValueError(f"unsupported dosing mode: {mode}")
    if mode == "ml_h":
        return round(value, 2)
    conc = LIBRARY[drug].concentration_mg_ml
    if conc <= 0:
        raise ValueError("mass-based dosing needs a concentration")
    if mode == "mcg_kg_min":
        if weight_kg is None or not 0 < weight_kg <= MAX_WEIGHT_KG:
            raise ValueError("weight-based dosing needs a patient weight in kg")
        mg_per_h = value * weight_kg * 60 / 1000
        return round(mg_per_h / conc, 2)
    return round(value / conc, 2)


def program_rate(drug: str, mode: str, value: float, weight_kg: float = None) -> dict:
    rate = to_ml_per_hour(drug, mode, value, weight_kg)
    return {"rate_ml_h": rate, "limit": check_rate(drug, rate), "needs_confirmation": True}

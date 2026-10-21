"""Therapy event log (SPEC-LOG-01). In-memory stand-in for the non-volatile log."""
import time

EVENTS = []


def log(event: str, **data):
    EVENTS.append({"t": time.time(), "event": event, **data})

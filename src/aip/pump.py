"""Delivery interlock and cassette latch (SPEC-PUMP-01)."""


class Pump:
    def __init__(self):
        self.latch_closed = False
        self.running = False
        self.clamp_engaged = True

    def set_latch(self, closed: bool):
        self.latch_closed = closed
        if not closed:
            self.stop()

    def start(self) -> bool:
        if not self.latch_closed:
            return False
        self.running, self.clamp_engaged = True, False
        return True

    def stop(self):
        self.running, self.clamp_engaged = False, True

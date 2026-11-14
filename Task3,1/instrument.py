from config import InstrumentConfig
from sources import SignalSource

MAX_SAMPLE_RATE = 100_000.0
ALLOWED_RANGES = (1.0, 5.0, 10.0, 50.0)

class Instrument:
    def __init__(self, config: InstrumentConfig, source: SignalSource):
        self._source = source
        self._resolution = config.resolution
        self._unit = config.unit
        self._channel = config.channel

        self.sample_rate = config.sample_rate
        self.measurement_range = config.measurement_range

        self._measurements: list[float] = []
        self._is_closed = False

    @property
    def sample_rate(self) -> float:
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, value: float):
        if value <= 0 or value > MAX_SAMPLE_RATE:
            raise ValueError(f"Your value cannot be greate them {MAX_SAMPLE_RATE}")
        self._sample_rate = float(value)

    @property
    def measurement_range(self) -> float:
        return self._measurement_range

    @measurement_range.setter
    def measurement_range(self, value: float):
        if value not in ALLOWED_RANGES:
            raise ValueError("This range is not allowed!")
        self._measurement_range = float(value)
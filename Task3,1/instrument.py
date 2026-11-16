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

    def _check_open(self):
        if self._is_closed:
            raise RuntimeError("Instrument is closed. Another use is prohibited!")

    def measure_one(self) -> float:
        self._check_open()
        value = self._source.read_sample()
        if abs(value) > self.measurement_range:
            raise ValueError(f"Value {value} is not in {self.measurement_range}")
        self._measurements.append(value)
        return value

    def measure_series(self, n: int) -> list[float]:
        self._check_open()
        if type(n) is not int or n <= 0:
            raise ValueError("The amount of measurements must be positive, whole number")
        return [self.measure_one() for _ in range(n)]

    def status(self) -> dict:
        return {
            "channel": self._channel,
            "is_closed": self._is_closed,
            "sample_rate": f"{self._sample_rate} Hz",
            "measurement_range": self.measurement_range,
            "measurement_count": len(self._measurements),
        }

    def close(self):
        self._is_closed = True

    def __enter__(self):
        self._check_open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False

    def __repr__(self) -> str:
        state = "closed" if self._is_closed else "open"
        return (
            f"Instrument(channel='{self._channel}', range={self.measurement_range}, "
            f"rate={self.sample_rate} Hz, samples={len(self._measurements)}, state='{state}'"
        )

    def __len__(self) -> int:
        return len(self._measurements)

    def save_to_file(self, file_path: str, signal_shape: str = "sine_with_noise"):
        seed_val = self._source._seed if isinstance(self._source, SignalSource) else None
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# sample_rate: {self.sample_rate} Hz\n")
            f.write(f"# unit: {self._unit}\n")
            f.write(f"# signal_shape: {signal_shape}\n")
            if seed_val is not None:
                f.write(f"# seed: {seed_val}\n")
            for val in self._measurements:
                f.write(f"{val}\n")
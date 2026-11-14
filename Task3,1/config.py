from dataclasses import dataclass

@dataclass
class InstrumentConfig:
    sample_rate: float
    measurement_range: float
    resolution: int
    unit: str
    channel: str
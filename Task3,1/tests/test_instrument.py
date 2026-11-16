import pytest

from config import InstrumentConfig
from instrument import Instrument
from sources import SyntheticSource, FileSource

def make_config() -> InstrumentConfig:
    return InstrumentConfig(
        sample_rate = 500.0,
        measurement_range = 5.0,
        resolution = 16,
        unit = "V",
        channel = "TEST_CH",
    )

def test_series_length():
    config = make_config()
    device = Instrument(config, SyntheticSource(seed=1))
    data = device.measure_series(15)
    assert len(data) == 15
    assert len(device) == 15

def test_values_within_range():
    config = make_config()
    device = Instrument(config, SyntheticSource(seed=10))
    data = device.measure_series(20)
    assert all(abs(val) <= config.measurement_range for val in data)

def test_context_manager_closes_device():
    config = make_config()
    with Instrument(config, SyntheticSource(seed=2)) as device:
        device.measure_one()
        assert device.status()["is_closed"] is False

    assert device.status()["is_closed"] is True
    with pytest.raises(RuntimeError):
        device.measure_one()

def test_invalid_settings_raise_error():
    bad_rate = InstrumentConfig(-10.0, 5.0, 12, "V", "CH1")
    with pytest.raises(ValueError):
        Instrument(bad_rate, SyntheticSource())

    bad_range = InstrumentConfig(100.0, 999.0, 12, "V", "CH1")
    with pytest.raises(ValueError):
        Instrument(bad_range, SyntheticSource())
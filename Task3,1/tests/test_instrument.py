import pytest

from ..config import InstrumentConfig
from ..instrument import Instrument
from ..sources import SyntheticSource, FileSource

@pytest.fixture
def valid_config():
    return InstrumentConfig(
        sample_rate = 500.0,
        measurement_range = 5.0,
        resolution = 16,
        unit = "V",
        channel = "TEST_CH",
    )

def test_series_length(valid_config):
    device = Instrument(valid_config, SyntheticSource(seed=1))
    data = device.measure_series(15)
    assert len(data) == 15
    assert len(device) == 15

def
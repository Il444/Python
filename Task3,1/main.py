from config import InstrumentConfig
from sources import SyntheticSource, FileSource
from instrument import Instrument

def main():
    config = InstrumentConfig(
        sample_rate = 1000.0,
        measurement_range = 5.0,
        resolution = 12,
        unit = "V",
        channel = "Ch1",)

    synth_source = SyntheticSource(seed=42)
    output_file = "sample_measurements.txt"

    with Instrument(config, synth_source) as  device:
        print("Instrument is working", repr(device))
        series = device.measure_series(10)
        print(f"Made {len(device)} measurements ({config.unit}):", [round(x, 4) for x in series])

        device.save_to_file(output_file)
        print("Condition before closing: ", device.status())

    print("Condition after with: ", repr(device))

    print("Reading saved files through FileSource")
    file_source = FileSource(output_file)
    with Instrument(config, file_source) as read_device:
        restored = read_device.measure_series(5)
        print(f"The first 5 measurements from file was read: ", [round(x, 4) for x in restored])

if __name__ == "__main__":
    main()
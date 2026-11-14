from abc import ABC, abstractmethod
import random
import math

class SignalSource(ABC):
    @abstractmethod
    def read_sample(self) -> float:
        pass

class SyntheticSource(SignalSource):
    def __init__(self, seed: int | None = None):
        self._rng = random.Random(seed)
        self._step = 0
        self.seed = seed 
    def read_sample(self) -> float:
        result = math.sin(self._step * 0.1)
        result += self._rng.uniform(-0.05, 0.05)
        self._step += 1
        return result

class FileSource(SignalSource):
    def __init__(self, file_path):
        self._index = 0
        with open(file_path, "r", encoding="utf-8") as f:
            self._samples = []
            for line in f:
                cleaned = line.strip()
                if not cleaned or cleaned.startswith("#"):
                    continue
                else:
                    self._samples.append(float(cleaned))
    def read_sample(self) -> float:
        if self._index >= len(self._samples):
            raise StopIteration("This is the end!")
        val = self._samples[self._index]
        self._index += 1
        return val
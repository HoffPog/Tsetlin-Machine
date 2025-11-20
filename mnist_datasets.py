import struct
import numpy as np
from typing import Tuple

class MNISTLoader:
    def __init__(self, data_dir: str = '.'):
        self.data_dir = data_dir
        # default filenames expected in workspace
        self.train_images = f"{data_dir}/train-images-idx3-ubyte"
        self.train_labels = f"{data_dir}/train-labels-idx1-ubyte"
        self.test_images = f"{data_dir}/t10k-images-idx3-ubyte"
        self.test_labels = f"{data_dir}/t10k-labels-idx1-ubyte"

    def _read_images(self, path: str) -> np.ndarray:
        with open(path, 'rb') as f:
            magic, num, rows, cols = struct.unpack('>IIII', f.read(16))
            data = np.frombuffer(f.read(), dtype=np.uint8)
            data = data.reshape(num, rows * cols)
            return data

    def _read_labels(self, path: str) -> np.ndarray:
        with open(path, 'rb') as f:
            magic, num = struct.unpack('>II', f.read(8))
            data = np.frombuffer(f.read(), dtype=np.uint8)
            return data

    def load(self, train: bool = True) -> Tuple[list, list]:
        if train:
            imgs = self._read_images(self.train_images)
            labs = self._read_labels(self.train_labels)
        else:
            imgs = self._read_images(self.test_images)
            labs = self._read_labels(self.test_labels)

        # convert to python lists to match expected usage
        return imgs.tolist(), labs.tolist()

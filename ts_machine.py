from mnist_datasets import MNISTLoader
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

loader = MNISTLoader()
images, labels = loader.load()
assert len(images) == 60000 and len(labels) == 60000

train_images, train_labels = loader.load(train=False)
assert len(train_images) == 10000 and len(train_labels) == 10000

img = images[1]
label = labels[1]

img_reshaped = img.reshape(28, 28)
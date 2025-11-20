from mnist_datasets import MNISTLoader
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from ts_automata import Automata

loader = MNISTLoader()
images, labels = loader.load()
assert len(images) == 60000 and len(labels) == 60000

train_images, train_labels = loader.load(train=False)
assert len(train_images) == 10000 and len(train_labels) == 10000

img = images[1]
label = labels[1]

#convert to boolean features
def booleanize(arr: list):
    for i,pixel_val in enumerate(arr):
        if pixel_val > 0:
            arr[i] = 1
        else:
            arr[i] = 0
    return arr

a_1 = Automata()



#kind of pointless, for visualisation
img_reshaped = booleanize(img)
print(img_reshaped)
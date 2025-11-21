from mnist_datasets import MNISTLoader
import numpy as np
from PIL import Image
from ts_automata import Automata
from ts_class import Class
import timeit
import random
a = '''
from math import sqrt
def example():
    mylist = [sqrt(x) for x in range(100)]
'''
t = timeit.timeit(a, number=1000000) * 1e3

loader = MNISTLoader()
images, labels = loader.load()
assert len(images) == 60000 and len(labels) == 60000

train_images, train_labels = loader.load(train=False)
assert len(train_images) == 10000 and len(train_labels) == 10000

# img = images[1]
# label = labels[1]

class_scores = []

#convert to boolean features
def booleanize(arr: list):
    # for i,pixel_val in enumerate(arr):
    #     if pixel_val > 0:
    #         arr[i] = True
    #     else:
    #         arr[i] = False
    # return arr
    return [pixel_val > 0 for pixel_val in arr]


#Spawn our 10 classes for 0-9
classes = []
for x in range(10):
    classes.append(Class())

#Spawn the clauses and automatons for each class
# c = 0
# for v in classes:
#     v.spawn_class(len(images[1])*2, 5, 150, c)
#     c += 1

c = 0
for v in classes:
    v.spawn_class(len(images[1]), 10, 100, c)
    c+= 1



DEBUG_ARR = []

#TRAINING
for i in range(10):
    for x in range(1000):
        l = random.randint(1,1000)
        img = images[l]
        label = labels[l]
        bool_features = booleanize(img)

        class_scores = []
        for v in classes:
            score = v.eval_class(bool_features, True, 150)
            class_scores.append(score)

        # Provide feedback to all classes
        # for i, v in enumerate(classes):
        #     y_c = 1 if i == int(label) else 0
        #     v.train_downstream(y_c)

        # Train the class the data belonged to.
        for i, v in enumerate(classes):
            if v.index == int(label):
                y_c = False
                v.train_downstream(y_c)
            
        # Train a random class
        r = random.randint(0,9)
        if classes[r].index == int(label):
            y_c = True
            classes[r].train_downstream(y_c)
        else:
            y_c = False
            classes[r].train_downstream(y_c)



print("Training Done.")

runs = []

#EVALUATE


eval_score = 0
for x in range(1000):
    l = x+1000
    img = images[l]
    label = labels[l]
    bool_features = booleanize(img)

    class_scores = [v.eval_class(bool_features, False, 150) for v in classes]
    top_class = class_scores.index(max(class_scores))
    if classes[top_class].index == int(label):
        eval_score += 1

accuracy = eval_score / 100 * 100
print(f"Accuracy: {accuracy:.2f}%")
print(round(t, 3), "ms")
runs.append(accuracy)

# print("------------------")
# print(f"{runs}")
# print("------------------")
t = timeit.timeit(a, number=1000000) * 1e3
print(round(t, 3), "ms")

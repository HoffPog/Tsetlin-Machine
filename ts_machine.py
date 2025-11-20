from mnist_datasets import MNISTLoader
import numpy as np
from PIL import Image
from ts_automata import Automata
from ts_class import Class

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
    for i,pixel_val in enumerate(arr):
        if pixel_val > 0:
            arr[i] = True
        else:
            arr[i] = False
    return arr

#Spawn our 10 classes for 0-9
classes = []
for x in range(10):
    classes.append(Class())

#Spawn the clauses and automatons for each class
for v in classes:
    v.spawn_class(len(images[1])*2, 5, 150)

#TEST on the first 100 images
for x in range(100):

    img = images[x]
    label = labels[x]
    bool_features = booleanize(img)

    for v in classes:
        score = v.eval_class(bool_features, True, 150)

        class_scores.append(score)
        print(f"[TRAIN] Score of class {v.index} -> ({score}) ")

    #find the top scoring class
    top_class = class_scores.index((max(class_scores)))
    print(f"[TRAIN] Top class: {v.index}")
    print(class_scores)

    for v in classes:
        if (int(label) == class_scores) and (v.index is top_class):
            v.train_downstream(True)
        else:
            v.train_downstream(False)

    class_scores = [] #reset scores

eval_score = 0
        
#EVALUATE on the same 100 images for accuracy
for x in range(100):

    img = images[x]
    label = labels[x]
    bool_features = booleanize(img)

    for v in classes:
        score = v.eval_class(bool_features, True, 150)

        class_scores.append(score)
        print(f"Score of class {class_scores.index(score)} -> ({score}) ")

    #find the top scoring class
    top_class = class_scores.index((max(class_scores)))
##############
    for v in classes:
        if (v.index is top_class):
            if (v.index == int(label)):
                print(f"SUCCESS on identifying: {label}")
                eval_score += 10
        else:
            print(f"FAILED on identifying: {label}")

print(f"Overall success rate: {eval_score}")
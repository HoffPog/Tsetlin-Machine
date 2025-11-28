from mnist_datasets import MNISTLoader
import numpy as np
from PIL import Image
from ts_automata import Automata
from ts_class import Class
import timeit
import random
import matplotlib.pyplot as plt

loader = MNISTLoader()
images, labels = loader.load(train=True)
assert len(images) == 60000 and len(labels) == 60000

test_images, test_labels = loader.load(train=False)
assert len(test_images) == 10000 and len(test_labels) == 10000

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

CLASS_SCORE_HISTORY = []

indices = list(range(len(images)))
random.shuffle(indices)
ccc = 0
#TRAINING
for epoch in range(10):

    for image_num in range(100):

        train_index = image_num
        img = images[train_index]
        label = labels[train_index]
        bool_features = booleanize(img)

        class_scores = []
        for v in classes:
            score = v.eval_class(bool_features)
            #print(f"C_score: {score}")
            class_scores.append(score)

        # Provide feedback to all classes
        # for i, v in enumerate(classes):
        #     y_c = 1 if i == int(label) else 0
        #     v.train_downstream(y_c)
 
        # Train the class the data belonged to.
        for i, k in enumerate(classes):
            if k.index == int(label):
                y_c = False
                k.train_downstream(y_c)
                #print(f"Real Class Training: {k.index}")

        # for i, k in enumerate(classes):
        #     y_c = (k.index == int(label))
        #     k.train_downstream(y_c)

        
            
        # Train a random class
        r = random.randint(0,9)
        if classes[r].index == int(label):
            y_c = True
            classes[r].train_downstream(y_c)
            #print(f"Real Random Class Training: {r}")
        else:
            y_c = False
            classes[r].train_downstream(y_c)
            #print(f"False Random Class Training: {r}")

        print(f"Iter: {ccc}, Epoch: {epoch}, Label: {label} | {class_scores}")

        CLASS_SCORE_HISTORY.append(class_scores)

        ccc += 1

    print(f"Epoch: {epoch} | {class_scores}")

    # CLASS_SCORE_HISTORY.append(class_scores)


print("Training Done.")

runs = []

#EVALUATE

DEBUG_class_guesses = [0,0,0,0,0,0,0,0,0,0]

eval_score = 0
for image_no in range(100):
    l = image_no
    img = test_images[l]
    label = test_labels[l]
    bool_features = booleanize(img)

    class_scores = [v.eval_class(bool_features) for v in classes]
    top_class = class_scores.index(max(class_scores))
    print(f"{label} | Winner: {top_class} | {class_scores}")

    DEBUG_class_guesses[top_class] += 1

    if top_class == int(label):
        eval_score += 1

accuracy = eval_score / len(test_images) * 100
print(f"Accuracy: {accuracy:.2f}%")
runs.append(accuracy)
print(DEBUG_class_guesses)

# print("------------------")
# print(f"{runs}")
# print("------------------")
# t = timeit.timeit(a, number=1000000) * 1e3
# print(round(t, 3), "ms")

CLASS_SCORE_HISTORY = np.array(CLASS_SCORE_HISTORY)
epochs = CLASS_SCORE_HISTORY.shape[0]

for cls in range(CLASS_SCORE_HISTORY.shape[1]):
    plt.plot(
        range(epochs),
        CLASS_SCORE_HISTORY[:, cls],
        label=f"Class {cls}"
    )

plt.xlabel("Image Count")
plt.ylabel("Class score")
plt.title("Class scores throughout training")
plt.legend()
plt.grid(True)
plt.show()
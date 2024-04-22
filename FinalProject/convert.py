import numpy as np
from PIL import Image
import os

def load_images(directory,start, end):
    images = []
    array = np.linspace(start, end,end,dtype=int)
    for i in array:
        filename = f"/img_{i}.png"
        if ((i%100)==0):          
            print(i)
            print(filename)
        img = Image.open(directory + filename)
        img_array = np.array(img)
        images.append(img_array)
    return images

X_train_i = load_images("Data/train_data_unlabeled/train_data_unlabeled", 1, 16182) 
X_test_i = load_images("Data/test_data_unlabeled/test_data_unlabeled",1, 4796)
np.savez('Data/data.npz',X_train=X_train_i,X_test=X_test_i)
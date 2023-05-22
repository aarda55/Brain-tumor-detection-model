import numpy as np
import matplotlib.pyplot as plt
import os 
import cv2
import random
import pickle
import time

#defines catagories for seperation
DATADIR = "C:\\Users\\ardaa\\OneDrive\\Desktop\\archive\\BrainT-Dataset"
CATEGORIES = ["glioma","meningioma", "notumor", "pituitary"]
IMG_SIZE = 50

training_data = []

#formats data
def create_training_data():
   for category in CATEGORIES:
      path = os.path.join(DATADIR, category)
      class_num = CATEGORIES.index(category)
      for img in os.listdir(path):
          try:
              img_array = cv2.imread(os.path.join(path,img))
              new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
              training_data.append([new_array, class_num])
          except Exception as e:
              pass

#creates data as lists
create_training_data()
random.shuffle(training_data)
X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 3)



#saves data in pickle files for training of the model
pickle_out = open("X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()
import cv2
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

data = []
labels = []

dataset_path = "dataset"

for label in os.listdir(dataset_path):
    folder = os.path.join(dataset_path, label)

    for img_name in os.listdir(folder):
        img_path = os.path.join(folder, img_name)

        img = cv2.imread(img_path)
        img = cv2.resize(img, (64, 64))  # reduzir tamanho
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        data.append(img.flatten())
        labels.append(label)

data = np.array(data)
labels = np.array(labels)

model = RandomForestClassifier(n_estimators=100)
model.fit(data, labels)

joblib.dump(model, "model.pkl")

print("Modelo treinado!")
from skimage.feature import hog
from skimage.io import imread
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import numpy as np
import os
import time
import csv
import pandas as pd

# Reading the csv file into a Dataframe
df = pd.read_csv("/training.csv")

# Creating a list of lists from the Dataframe
training = [list(row) for row in df.values]
print(training)


def calculate_HOG(rootdir, noOfElementsSkipped):
    data = []
    labels = []

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            path = os.path.join(subdir, file)
            fileNo = int(path[-8:-4])
            if noOfElementsSkipped != 0:
                if (fileNo % noOfElementsSkipped != 0):
                    continue
            img = imread(path, as_gray=True)
            feature = hog(img, feature_vector=True)
            data.append(feature)
            isPositive = False
            if "positive" in path:
                isPositive = True
            if isPositive is True:
                labels.append(1)
            else:
                labels.append(0)

    return np.array(data), labels


start = time.process_time()

print("Obtaining pedestrian HOG features training and test data...")
noOfElementsSkipped = 150
trainData, trainLabels = calculate_HOG(
    "./Individual/train/", noOfElementsSkipped)
testData, testLabels = calculate_HOG("./Individual/test/", noOfElementsSkipped)

print("Training the pedestrian Linear SVM classifier...")
clf = LinearSVC()
clf.fit(trainData, trainLabels)

# print(" Training KNN classifier...")
# clf = KNeighborsClassifier()
# clf.fit(trainData, trainLabels)

print("Evaluating the classifier on the pedestrian test data...")
pred = clf.predict(testData)
print(classification_report(testLabels, pred))
runTime = (time.process_time() - start)
print("Run time: ", runTime)

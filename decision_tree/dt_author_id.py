#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
from sklearn.tree import DecisionTreeClassifier

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

print "Features:", len(features_train[0])

clf = DecisionTreeClassifier(min_samples_split=40)

train_time = time()
clf.fit(features_train, labels_train)
print "Training time:", round(time()-train_time, 3), "s"

score_time = time()
print "Accuracy:", clf.score(features_test, labels_test)
print "Score time:", round(time()-score_time, 3), "s"

#########################################################

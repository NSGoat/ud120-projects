#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
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

from sklearn import svm

clf = svm.SVC(kernel='rbf', C=10000.0)

train_time = time()
print "\nBeginning training (Kernel: ", clf.kernel, "C: ", clf.C, "Gamma ", clf.gamma, ")"

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

clf.fit(features_train, labels_train)
print "Training time:", round(time()-train_time, 3), "s"

test_time = time()
accuracy = clf.score(features_test, labels_test)
print "Testing time:", round(time()-test_time, 3), "s"
print "Accuracy: ", accuracy

predictions = clf.predict(features_test)
print "Element 10:", predictions[10]
print "Element 26:", predictions[26]
print "Element 50:", predictions[50]

sara = filter(lambda x: x==0, predictions)
chris = filter(lambda x: x==1, predictions)

print "Sara:", len(sara)
print "Chris:", len(chris)
#########################################################

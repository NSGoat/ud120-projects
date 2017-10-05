#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL", 0) # Remove outlier
data = featureFormat(data_dict, features)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

# Determine the label for the most obvious outlier
#     if bonus > 97343610:
#         # print point
#         # print data_dict
#         for key in data_dict:
#             if data_dict[key]["bonus"] == bonus:
#                 print key
#                 print data_dict[key] # prints TOTAL


# Determine the labels for the other obvious outliers
# people = []
# for name in data_dict:
#     entry = data_dict[name]
#     person = (name, entry["bonus"], entry["salary"])
#     if entry["bonus"] != "NaN" and entry["salary"] != "NaN":
#         # if entry["bonus"] > 5000000 and entry["salary"] > 1000000:
#         #     print person
#         people.append(person)
# people = sorted(people, key=lambda x: x[1])
# print people[len(people)-4:]

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

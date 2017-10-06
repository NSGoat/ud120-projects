#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()

print "\nBeginning"

### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

# Filter out items that are missing values for exercised_stock_options
data_dict = {k: v for k, v in data_dict.items() if v["exercised_stock_options"] != "NaN" }

# Find min and max exercised_stock_options
key_min_stock = min(data_dict, key=lambda k: data_dict[k]["exercised_stock_options"])
key_max_stock = max(data_dict, key=lambda k: data_dict[k]["exercised_stock_options"])
print key_min_stock, data_dict[key_min_stock]["exercised_stock_options"], "exercised_stock_options min"
print key_max_stock, data_dict[key_max_stock]["exercised_stock_options"], "exercised_stock_options max"

# Filter out items that are missing values for salary
# data_dict = {k: v for k, v in data_dict.items() if v["salary"] != "NaN" }

# Find min and max saleries
key_min_salary = min(data_dict, key=lambda k: data_dict[k]["salary"])
key_max_salary = max(data_dict, key=lambda k: data_dict[k]["salary"])
print key_min_salary, data_dict[key_min_salary]["salary"], "salary min"
print key_max_salary, data_dict[key_max_salary]["salary"], "salary max\n"

feature_1 = "salary"
feature_2 = "exercised_stock_options"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )

# Perform feature scaling on salary and exercised_stock_options
finance_features.append(numpy.array([200000., 1000000]))
print "Quiz",  finance_features[-1]
print finance_features
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
finance_features = scaler.fit_transform(finance_features)
print "Min:", scaler.data_min_, "Max:", scaler.data_max_
print "Quiz", finance_features[-1]

### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2, n_init=10, max_iter=300)
kmeans.fit(finance_features)
pred = kmeans.labels_


### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"

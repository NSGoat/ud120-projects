#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# All people in data set
print "Total people:", len(enron_data)
# Print all people in data set
# for k in enron_data:
#     print k, "\n", enron_data[k], "\n\n"


# People of interest
pois = {k: v for k, v in enron_data.iteritems() if v['poi'] == True}
print "People of interest:", len(pois)
# Print People of interest
# for k in pois:
#     print k, "\n", pois[k], "\n\n"

# print enron_data["PRENTICE JAMES"]["total_stock_value"]
# print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
# print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "CEO: SKILLING JEFFREY K", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Chairman: LAY KENNETH L", enron_data["LAY KENNETH L"]["total_payments"]
print "CFO: FASTOW ANDREW S", enron_data["FASTOW ANDREW S"]["total_payments"]


people_with_email = {k: v for k, v in enron_data.iteritems() if v["email_address"] != "NaN"}
print "People with email address:", len(people_with_email)

people_with_salary = {k: v for k, v in enron_data.iteritems() if v["salary"] != "NaN"}
print "People with salary:", len(people_with_salary)


people_with_total_payments = {k: v for k, v in enron_data.iteritems() if v["total_payments"] == "NaN"}
percentage = float(len(people_with_total_payments)) / float(len(enron_data)) * 100.0
print "People without total_payments:", len(people_with_total_payments), percentage, "%"

pois_with_total_payments = {k: v for k, v in pois.iteritems() if v["total_payments"] == "NaN"}
percentage = float(len(pois_with_total_payments)) / float(len(pois)) * 100.0
print "People of interest without total_payments:", len(pois_with_total_payments), percentage

# Jacob Crawford
# Data Engineering December
# Jan 6, 2023
import json
import random
from typing import List

import numpy as np

# 1
sen = "The quick brown fox jumped over the lazy dog"
print(sen)

print("type of sen is: ", type(sen))


def assign_to_vars(sentence: object) -> object:
    list_sen = []
    for wd in sentence.split(" "):
        list_sen.append(wd)
    return list_sen


print(assign_to_vars(sen))
lst1 = (a, b, c, d, e, f, g, h, i) = assign_to_vars(sen)
print(lst1)
print("type of lst1 is ", type(lst1))
# 10
lst2 = (a2, b2, c2, d2, e2, f2, g2, h2, i2) = sen.split(" ")
print("type of lst2 is ", type(lst2))

sen2 = " ".join(lst2)

print("sen2: ", sen2)

word = "Hello World"
another_word = ", I love Python"
dct = {"hello": word, "love": another_word}
print(dict)

e1 = dct["hello"]
print(e1)
print(dct["love"])

# 16 Hell or Python
print(word[0:4], word[-4:-2], another_word[-6:])

# 17)

dict2 = {'a3': a2, 'b3': b2, 'c3': c2, 'd3': d2, 'e3': e2, 'f3': f2, 'g3': g2, 'h3': h2, 'i3': i2}

print(dict2)
print("dict2 type is: ", type(dict2))

sen3 = ''
for i in dict2.values():
    sen3 = sen3 + " " + i

print("sen3: ", sen3)
# 21
us_trucks1 = {'make': 'Ford', 'model': 'F-150'}
# 22
us_trucks2 = {'make': 'Chevrolet', 'model': 'Silverado'}
# 23
us_trucks3 = {'make': 'Dodge', 'model': 'Ram 1500'}
# 24
us_trucks4 = {'make': 'Jeep', 'model': 'Gladiator'}
# 25
print(us_trucks2)
# 26
print(us_trucks3['make'])
# 27
us_trucks_list = [us_trucks4, us_trucks3, us_trucks2, us_trucks1]
# 28
print(us_trucks_list)
# 29
print("second in the list: ", us_trucks_list[1])
# 30
# ERRORS: print(us_trucks_list[0][1])
print("make of the first model in the list: ", us_trucks_list[0]['make'])
# 31
print(us_trucks_list[0]['make'])
# 32
print(us_trucks_list[0]['model'])
# 33 Find and print the element in the list where the truck is made by Chevrolet.
for mk in us_trucks_list:
    if mk['make'] == 'Chevrolet':
        print("model made by Chevrolet is the ", mk['model'])
# 35
for mk in us_trucks_list:
    if mk['make'] == 'Jeep':
        print("model made by Jeep is the ", mk['model'])
# 36
testFailure = us_trucks1.update(us_trucks2)
print(testFailure)

# 37
dict1 = {'Dodge': 'Ram 150'}
# 38
dict2 = {'Ford': 'F-150'}
# 39
print(dict1)
# 40
print(dict2)
# 41
dict1.update(dict2)
# 42
print(dict1)
# 43
print(dict2)
# 44
dict1 = {'Dodge': 'Ram 150'}  # reset
# 45
dict2 = {'Ford': 'F-150'}
# 46
var1 = {**dict1,
        **dict2}  # With ** you don't change dict 1 or dict2,
# but if you want to see the result you need another variable
# 47
dict3 = {**dict1, **dict2}
# 48)
print(dict1)

# 49)
print(dict2)

# 50)
print(dict3)
# 51
file = open('../new_families.txt', "r")

# 52
print("version #52")
print("can I read these contents? ", file)  # I cannot read it. It's type TextIOWrapper
print("file is of type ", type(file))
file.close()

# 53
# The file is of type TextIOWrapper.
print("version #53: ")
file2 = open("../new_families.txt", "r")
family_file = file2.read()
print("This is the #53 version: ")
print(family_file)
file2.close()
# #54
print("this is the #54 version: ")
for f in open("../new_families.txt", "r"):
    json_in = f.replace("'", '"')
    new_f = json.loads(json_in)
print(new_f)
print("I'm getting a ", type(new_f))
file.close()
#
# # 55
print("This is the #55 version: ")
# #TextIOWrapper  -- below method works.
for ff in open("../new_families.txt", 'r'):
    print(type(ff))
    print("All I get is this single bracket :", ff[0])

#
# # 56
print("THis is the # 56 version: ")
# # # Python3 code to demonstrate working of
# # # Convert String to List of dictionaries
# # # Using json.loads + replace()
# #
# printing original string
print("The original string is : " + family_file)
#
# # replace() used to replace strings
# # loads() used to convert
file3 = open('../new_families.txt', 'r')
for wd in file3:
    json_in = wd.replace("'", '"')
    new_f = json.loads(json_in)
# printing result
print("Converted list of dictionaries : " + str(new_f))
#
# #57
print(" Printing #57 : ")
print(" ")
print("first element of the list is: ", new_f[1])

#
# 58)
new_lst1 = [1, 2, 3]

# 59)
new_lst2 = ['a', 'b', 'c']

# 60) Join new_lst1 and new_lst2 together to make a new variable, new_lst3.
new_list3 = new_lst1 + new_lst2
print("problem #60: ", new_list3)

# 61
# Generate a customer list consisting of at least 1000 customers to use for
# your capstone project. The data must include “firstname”, “lastname”, “street
# address”, “city”, “state”, “zip”, “phone”, and “email_address” (You might
# have to combine several datasets to get all the required data.) When you have
# that, add another column for “loyalty_acct” that contains random 6–7 digit
# integers. (you can generate this without searching on the internet. Think
# “loop”!)

loyalty_acct: list[int] = []
for i in range(3400):
    loyalty_acct.append(random.randint(100000, 999999))
print("sample of the loyalty acct #s: ", str(loyalty_acct[0:22]))

# the for loop is used to append the other 9 numbers.
# the other 9 numbers can be in the range of 0 to 9.
phone_numbers = []
for i in range(3400):
    phone_numbers.append(random.randint(1000000000, 9999999999))
print("sample of the phone numbers: ", phone_numbers[0: 5])

first_names = open("customer_first_names.txt", "r")
first_names_list = first_names.readlines()
email_list = []
for i in first_names_list:
    i = i[0:-1] + str(random.randint(1, 100))
    email_list.append(i + "@yahoo.com")
# print(email_list[0:100])

# writing emails to file
with open('email_list.txt', 'w') as f:
    for i in email_list:
        f.write(i + ', ')
file.close()

# opening up the locations, stripping space and newlines
with open('locations', "r") as z:
    locations = []
    for i in z:
        i.rstrip("\n").replace('\n', ',')
        locations.append(i[0:-1])

# print(locations[0: 11]) # a test to see the results
city_state = []
zip_codes = []  # separating the zips from the city/states
for i in range(0, len(locations)):
    if i % 2 == 0:
        zip_codes.append(locations[i] + ',')
    else:
        city_state.append(locations[i])

print("city state: ", city_state[0:4])
print("zip codes: ", zip_codes[0:4])

split_list = []  # parsing the cities from the states
for i in city_state:
    split_list.append(i.split(","))
print("split list: ", split_list[0:22])
print("city_state ", city_state[0:5])

# Cities text file has been written.
with open('cities.txt', 'w') as f:
    for i in split_list:
        # print(i[0])
        f.write(i[0].rstrip(' ') + "\n")

# States text file has been written.
with open('states.txt', 'w') as f:
    for i in split_list:
        # print(i[0])
        f.write(i[1].rstrip() + "\n")
file.close()

########################
# WRITING THE DATA TO THE FINAL CSV file
########################
# loyalty account
# with open('customer_first_names.txt', "r") as f:
# first names - first_name_list
with open('last_names.txt') as f:
    last_name_final = []
    for i in f:
        last_name_final.append(i)

with open('street_addresses.txt', "r") as f:
    addresses_final = []
    for i in f:
        addresses_final.append(i)
print("addresses final: ", addresses_final[0])

print("len of 1st names: ", len(first_names_list))
with open('cities.txt', "r") as f:
    cities_final = []
    for i in f:
        cities_final.append(i)
print("cities final: ", cities_final[0:1])

with open('states.txt', "r") as f:
    states = []
    for i in f:
        states.append(i.rstrip() + ",")
print("states final: : ", states[0:1])

# the final writing:
with open('FinalData.csv', "w") as f:
    f.write("loyalty #," + "first," + "last," + "phone," + "address," + "city," + "state," + "zip,\n")
    for i in range(2500):
        f.writelines(str(loyalty_acct[i]) + ',' + first_names_list[i].rstrip('\n') + ',' + last_name_final[i].rstrip(
            '\n') + ',' + str(phone_numbers[i]) + ',' + addresses_final[i].rstrip('\n') + ',' + cities_final[i].rstrip(
            '\n') + ',' + states[i].rstrip('\n') + str(zip_codes[i] + '\n'))
f.close()

import csv

my_file = '../file/user.csv'
date = csv.reader(open(my_file, 'r', errors='ignore'))
for user in date:
    print(user)
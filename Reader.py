import csv
alist = list()
file = "file name here"

with open(file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in csv_reader:
        alist.append(i)


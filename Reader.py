import csv
alist = list()

with open(file name here, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in csv_reader:
        alist.append(i)


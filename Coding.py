import csv
alist = list()

with open('j1.5.in', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in csv_reader:
        alist.append(i)

    for i in range(0,1):
        if(alist[i] == 8 or alist[i] == 9):
            print("Ignore")
            break
        elif(alist[1]== alist[2]):
            print("Ignore")
            break
        if(alist[3]==8 or alist[3] == 9):
            print("Ignore")
            break
        else:
            print("Answer")
            break

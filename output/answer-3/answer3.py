import csv


def writer(a):
    with open("H:\\pythonProject\\internship-test2\\output\\answer-3\\main.csv", 'a+') as csv_out:
        csv_write = csv.writer(csv_out)
        csv_write.writerow(a)
c = -2
with open("H:\\pythonProject\\internship-test2\\input\\question-3\\main.csv", 'r+') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        c = c + 1
        strj = row[0]
        if strj == 'Team':
            writer([" ", "Team", "Yellow cards", "Red cards"])
        else:
            a=[c, strj, row[-5], row[-4]]
            writer(a)

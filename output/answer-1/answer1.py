import csv
def writer(a):
    with open("H:\\pythonProject\\internship-test2\\output\\answer-1\\main.csv", 'a+') as csv_out:
        csv_write = csv.writer(csv_out)
        csv_write.writerow(a)

with open("H:\\pythonProject\\internship-test2\\input\\question-1\\main.csv", 'r+') as csv_file:

    reader = csv.reader(csv_file)

    for row in reader:
        strj=row[0]
        if strj.isdigit():
            if int(strj)%10==0:
                writer(row)

        else:
            writer(row)
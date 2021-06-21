import csv

with open('filename.csv', 'r') as csv_file: #read
    csv_reader = csv.reader(csv_file)

    with open('new_name.csv', 'w') as new_file: #write
        csv_writer = csv.writer(new_file, delimite='-')
    
    for line in csv_reader:
        # print(line[2])
        csv_writer.writerow(line)
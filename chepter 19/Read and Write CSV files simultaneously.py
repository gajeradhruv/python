# reader ,DR
# writer, Dialectors
from csv import DictReader, DictWriter
with open('file.csv', 'r') as rf:
    with open('output.csv', 'w', newline='') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf, fieldnames=['first_name', 'last_name', 'email'])
        csv_writer.writeheader()
        for Row in csv_reader:
         fname,lname,age=Row['first_name'],Row['last_name'],Row['age']
         csv_writer.writerow({
                'first_name':fname.upper(),
                'last_name':lname.upper(),
                'age':age
         })
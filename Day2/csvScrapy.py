import csv
MOCK_DATA = "../MOCK_DATA.csv"

'''     
with open(MOCK_DATA,'a',newline='') as csvfile:
    # Write
    writer = csv.writer(csvfile,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([3,'James','Camping','Male', 'Taiwan'])
'''
'''
# List Reader
with open(MOCK_DATA,newline='') as csv_file:
    # Read 
    reader = csv.reader(csv_file,delimiter=",")
    for row in reader:
        print(', '.join(row))
'''

#Dict Writer
with open(MOCK_DATA,'a',newline='') as csvfile:
    fieldnames = ['James','Jimy','fdf','df','fd']
    writer = csv.DictWriter(csvfile,fieldnames,delimiter=',',quotechar='"') 
    writer.writerow({
        'James':4,
        'Jimy':'Amy',
        'fdf':'Cheng',
        'df':'Female',
        'fd': 'USA'
    })

# Dict Reader
with open(MOCK_DATA,newline='') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=',',quotechar='"')
    for row in reader:
        print(row['Jimy'],row['fdf'])

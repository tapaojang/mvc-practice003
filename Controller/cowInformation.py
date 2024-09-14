import csv
csv_path = 'Model/cowInform.csv'
def cowInformation():
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile)
        cow = []
        for row in reader:
            cow.append(row)
    return cow

def get_cow_color(cowId):
    cow = cowInformation()
    cowId_str = str(cowId) 
    for c in cow:
        if c['CowId'] == cowId_str:
            return c['CowColor']
    return 'Not Found'

def get_cow_age(cowId):
    cow = cowInformation()
    cowId_str = str(cowId) 
    for c in cow:
        if c['CowId'] == cowId_str:
            return c['CowAge']
    return 'Not Found'


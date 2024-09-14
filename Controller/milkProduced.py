from Controller.cowInformation import cowInformation
from Controller.cowInformation import get_cow_color
from Controller.cowInformation import get_cow_age
from Model.calculatePlainMilk import calculatePlainMilk
from Model.calculateChocoMilk import calculateChocoMilk
from Model.calculateStrawMilk import calculateStrawMilk
import re
def cowMilkProduced(cowId):
    color = get_cow_color(cowId)
    years , months = find_age(cowId)
    liters = 0
    if color == 'White':
        liters = calculatePlainMilk(years, months)
    elif color == 'Brown':
        liters = calculateChocoMilk(years)
    elif color == 'Pink':
        liters = calculateStrawMilk(months)
    return liters

def find_age(cowId):
    cowAge = get_cow_age(cowId)
    years_match = re.search(r'(\d+) years?', cowAge)
    months_match = re.search(r'(\d+) months?', cowAge)

    years_match = int(years_match.group(1)) if years_match else 0
    months_match = int(months_match.group(1)) if months_match else 0
    return years_match, months_match

def totalMilk():
    cows = cowInformation()
    total = 0
    for cow in cows:
        total += cowMilkProduced(cow['CowId'])
    return total





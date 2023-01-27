import csv 
from tinydb import TinyDB
from pprint import pprint
#Import from CSV to list of dictionaries
def fromCSV(filename:str)->list[dict]:
    """
    Imports a CSV file and returns a list of dictionaries
    args:
        filename: name of the file to import
    returns:
        list of dictionaries
    """
    data = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    return data

# Define a function to import tinydb from a dictionary
def fromDict(data:list[dict])->None:
    """
    Imports a list of dictionaries into a TinyDB
    args:
        data: list of dictionaries
    """
    db = TinyDB('db.json')
    pass


filename = 'users.csv'
data = fromCSV(filename)
pprint(data[:3])
    
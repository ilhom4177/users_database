import csv
from tinydb import TinyDB
import time

db = TinyDB('db.json', indent=4, separators=(',', ': '))
users_table = db.table('users')

def read_csv(filename: str) -> list[dict]:
    '''Reads a CSV file and returns a list of dictionaries.'''
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)
    

def insert_data(data: dict) -> int:
    '''Inserts data into the database.'''
    return users_table.insert(data)


users = read_csv('users.csv')
for user in users:
    user['id'] = int(user['id'])
    
    print(insert_data(user))

    # sleep
    # time.sleep(1)

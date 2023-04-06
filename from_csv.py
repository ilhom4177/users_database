import csv
from tinydb import TinyDB

db = TinyDB('db.json', indent=4, separators=(',', ': '))
users = db.table('users')

def read_csv(filename: str) -> list[dict]:
    '''Reads a CSV file and returns a list of dictionaries.'''
    pass

def insert_data(data: list) -> None:
    '''Inserts data into the database.'''
    pass


if __name__ == '__main__':
    data = read_csv('users.csv')
    insert_data(data)

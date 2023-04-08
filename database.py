from tinydb import TinyDB, Query
from tinydb.operations import delete

db = TinyDB('db.json', indent=4, separators=(',', ': '))
users_table = db.table('users')


User = Query()

def get_by_field(field: str, value: str):
    '''Returns a user by field'''
    return users_table.search(User[field].search(value))


def get_user_by_id(user_id):
    '''Returns a user by id'''
    pass

def get_user_by_email(email):
    '''Returns a user by email'''
    pass


def get_user_by_first_name(first_name):
    '''Returns a user by first name'''
    pass

def get_user_by_last_name(last_name):
    '''Returns a user by last name'''
    pass

def get_user_by_country(country):
    '''Returns a user by country'''
    pass

def get_users_full_name(user):
    '''Returns a user's full name'''
    pass

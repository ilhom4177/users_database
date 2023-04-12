from tinydb import TinyDB, Query
from tinydb.operations import delete

db = TinyDB('db.json', indent=4, separators=(',', ': '))
users_table = db.table('users')


User = Query()

def get_by_field(field: str, value: str):
    '''Returns a user by field'''
    return users_table.search(User[field].search(value))
print(get_by_field("first_name", "Nanice"))

def get_user_by_id(user_id):
    '''Returns a user by id'''
    return users_table.get(doc_id=user_id)
# print(get_user_by_id("4"))

def get_user_by_email(email):
    '''Returns a user by email'''
    return users_table.search(User.email == email)
# print(get_user_by_email("nquinane0@utexas.edu"))


def get_user_by_first_name(first_name):
    '''Returns a user by first name'''
    return users_table.search(User.first_name == first_name)
# print(get_user_by_first_name("Marshall"))

def get_user_by_last_name(last_name):
    '''Returns a user by last name'''
    return users_table.search(User.last_name == last_name)
# print(get_user_by_last_name("Brodest"))

def get_user_by_country(country):
    '''Returns a user by country'''
    return users_table.search(User.country == country)
# print(get_user_by_country("Russia"))

def get_users_full_name(user):
    '''Returns a user's full name'''
    full_name = users_table.get(doc_id=user)
    return f'{full_name["first_name"]} {full_name["last_name"]}'
# print(get_users_full_name("5"))



def update_user(user_id, field, value):
    '''Updates a user's field'''
    pass

def delete_user(user_id):
    '''Deletes a user'''
    pass

def add_user(user):
    '''Adds a user to the database'''
    pass

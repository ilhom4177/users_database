from tinydb import TinyDB,Query
from pprint import pprint
db = TinyDB('db.json',indent=4)
# Read the entire database
data = db.all()
# Count the female users
count = 0 
user = Query()

female_users = db.search((user['gender']=='Female') & (user['country']=='China'))


pprint(female_users)
print(len(female_users))


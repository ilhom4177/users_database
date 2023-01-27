from tinydb import TinyDB

db = TinyDB('db.json',indent=4)
# Read the entire database
data = db.all()
# Count the female users
count = 0 

for row in data:
    if row['gender']=='Female':
        count += 1

print(count)
# users_database

you should convert the csv file to json and store it in tinyDB.
This is a simple project to create a database of users and their information. It is a simple CRUD application. Convert CSV to JSON and store in tinyDB.

## Installation

```bash
pip install -r requirements.txt
```

## Database Requirements

- [x] convert CSV to JSON
- [x] store JSON in tinyDB
- [x] add user to database
- [x] delete user from database
- [x] update user information
- [x] search for user

## Database Structure

```json
{
    "users": {
        "1": {
            "id": "int",
            "first_name": "str",
            "last_name": "str",
            "email": "str",
            "gender": "str",
            "job": "str",
            "country": "str"
        }
    }
}
```

## project files

- [x] users.csv - users data in csv format
- [x] from_csv.py - convert csv to json and store in tinyDB
- [x] database.py - CRUD operations on database
- [x] users.json - users data in json format

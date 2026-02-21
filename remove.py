## showcasing how to delete documents

from tinydb import TinyDB, where

countries_db = TinyDB("ten_countries.json")
countries_table = countries_db.table(name="countries")

print(len(countries_table)) # should return 10 first time

countries_table.remove(doc_ids=[3, 5, 7])

print(len(countries_table)) # should be 7 now

countries_table.remove(where("population") < 300_000_000)

print(len(countries_table)) # now 2

countries_table.truncate() # deletes all documents

print(len(countries_table)) # down to 0

# deleting the table
countries_db.tables() # {'countries'}

countries_db.drop_table(name="countries")

countries_db.tables() # empty set
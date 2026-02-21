from pprint import pprint # JSON prety printing
from tinydb import TinyDB, where

# identify records changed by update.py
with TinyDB("ten_countries.json") as countries_db:
     countries_table = countries_db.table(name="countries")
     pprint(countries_table.search(where("location") == "Mexico"))


# DATA TO SHOW update.py WORKS
#[{'% of world': 1.6,
#  'date': '30 Jun 2025',
#  'location': 'Mexico',
#  'population': 130575786,
#  'source': 'National quarterly update'}]
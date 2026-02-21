# file to show how to update records in TinyDB

from tinydb import TinyDB, where

# create countries table using ten countries json file
with TinyDB("ten_countries.json") as countries_db:
    countries_table = countries_db.table(name="countries")

    # access and update the database
    countries_table.update(
        {"population": 130_575_786}, where("location") == "Mexico"
    )

    countries_table.update(
        {"source": "National quarterly update"},
        where("location") == "Mexico",
    )


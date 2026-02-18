### initializes database and creates documents

from csv import DictReader
from tinydb import TinyDB

# create countries database and add table
# indent 4 uses pretty printing in JSON
with TinyDB("countries.json", indent=4) as countries_db:
    countries_table = countries_db.table(name="countries")

    # add single doc
    countries_table.insert(
        {"location": "Vatican City", "population": 501}
        )

    ## add multiple docs at one time
    countries_table.insert_multiple(
        [
            {"location": "India", "population": 1_417_492_000},
            {"location": "China", "population": 1_408_280_000},
        ]
        )

    ## add multple from another file (countries_file.csv)
    with open("countries_file.csv", "r") as csv_source:
            reader = DictReader(csv_source)
            for row in reader:
                row["population"] = int(row["population"])
                countries_table.insert(row)
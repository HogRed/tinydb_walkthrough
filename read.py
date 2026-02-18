## code to query the database
## can also be done in REPL
from pprint import pprint
from tinydb import Query, TinyDB

# create db based on ten countries file
countries_db = TinyDB("ten_countries.json")
countries_table = countries_db.table(name="countries")

# create query instance
query = Query()
query_def = (query.population > 220_000_000) & (query.population < 250_000_000)

# answer questions
pprint(countries_table.search(query_def))

pprint(countries_table.search(query["% of world"] >= 17))

pprint(countries_table.get(doc_ids=[9, 10]))

# close db
countries_db.close()
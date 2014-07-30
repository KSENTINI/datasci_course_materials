import MapReduce
import sys

"""
Implement a relational join as a MapReduce query

Consider the following query:

	SELECT * 
	FROM Orders, LineItem 
	WHERE Order.order_id = LineItem.order_id

Your MapReduce query should produce the same result as this SQL query executed against an appropriate database. 
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: record
    # value: order_id
    key = record
    value = record[1]
    mr.emit_intermediate(value, key)

def reducer(key, list_of_records):
    # key: order_id
    # value: list of records
    order_rec = list_of_records[0]
    for rec in list_of_records[1:]:
        joined_rec = order_rec + rec
        mr.emit(joined_rec)
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

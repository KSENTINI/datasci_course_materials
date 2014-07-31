import MapReduce
import sys

"""
The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. 
Implement a MapReduce algorithm to check whether this property holds. 
Generate a list of all non-symmetric friend relationships.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person 
    # value: friend 
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)
    mr.emit_intermediate(value, key)

def reducer(key, list_of_records):
    # key: person 
    # value: list of friends
    #set_rec = list (set(list_of_records))
    for friend in list_of_records:
      if (list_of_records.count(friend) == 1):
        asym_friend = (key, friend )
        mr.emit(asym_friend)
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

from collections import OrderedDict
import json

from memory_profiler import profile

@profile()
def kk():
    a1 = [1,2,3,4,5,6,7,8,9]
    b1 = ['a','b','c','d','e','f','g','h','i']
    c1 = ['A','B','C','D','E','F','G','H','I']
    list_name = zip(a1,b1,c1)

    keys = ["name", "description","type"]
    js =  json.dumps({"List":[OrderedDict(zip(keys, tup)) for tup in list_name]})
    print js

kk()

from collections import ChainMap
address={"city":"kathmandu","state":"Bagmati","Country":"Nepal"}
employee={"name":"Ram","contact":985682228,"Age":21}
salary={"hourly":1000,"monthly":210000}
info = ChainMap(address, employee,salary)
print(info)
print("My name is "+str(info["name"])+" from "+str(info["city"])+" and I earn "+str(info["monthly"])+" rs monthly.")
print(str(list(info.keys())))#key list
print(str(list(info.values())))#value list

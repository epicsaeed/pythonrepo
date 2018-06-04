#assign keys:values to the dictionary
details = {
    "Name" : "Saeed",
    "ID"   : 100042012,
    "Enrolled" : 2015
}

dicB =  {
    "Name" : "Hamad",
    "ID" : 100042028,
    "Enrolled" : 2015
}

#adds a new key:value
details["University"]="KUSTAR"

#print the length on the dictionary (4)
print(len(details))

#print true or falses if it found the key in the dictionary
print("University" in details)

#loops the whole dictionay in search of a specific key
for key, value in details.items():
for item in details:
    if "ID" in details:
        print("found")
        print("value is:", details.get("ID", "none"))
    else:
        print("not found")

#prints every key with its corresponding value
for key,val in details.items():
    print (key, "=>", val)

#prints only the keys of the dict
keys = details.keys()
print (keys)

from collections import defaultdict
d = defaultdict(list)
d["1"].append(0)

d = {
    "1": [0],
    "2": ""
}

d = {}
if "1" not in d:
    d["1"] = []

d["1"].append(0)


#prints the dictionary "details"
print (details)


#updates dictionary (details) with the values of dicB
details.update(dicB)



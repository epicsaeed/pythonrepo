#from collections import Counter

#print(Counter("Adam Acosta"))

S = "NewStore"

def counter(string):
    a = {}
# count occurances of character
    for ltr in string: 
        a[ltr] = string.count(ltr)
# print the result
    for k in sorted(a):
        print (k + ': ' + str(a[k]))

counter(S)

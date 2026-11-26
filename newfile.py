#PRACTICE SET DICTIOnARIES AND SETS
#DICTIONARIES
marks = {
    "harry": 100,
    "maham": 50
}

print(marks,type (marks))
#you dont check keys as indexing like
#print[0]
#but you can index as a keys like print["harry""]
print(marks["maham"])
student = {"name": "Ali", "age": 20}

print(student.get("name"))
print(student.keys())
print(student.values())
print(student.items())
student.update({"age": 21})
print(student)
student = {"name": "Ali", "age": 20}

# Print keys
for key in student:
    print(key)

# Print values
for value in student.values():
    print(value)

# Print both
for key, value in student.items():
    print(key, value)
    #dictionary represent as { } not ( )
    #dictionary (an emty dictionary represents in curly bracket.
    a={ }
    print (type(a))
#SETS
    b=set( )
print(type(b))
    #Dont use { } in sets
s={4, 5, 6, 5, 8, 10, 110}
print (s)
e={4, 5, 6, 5, 8, 10, 110, "duaa"}
print (e, type(e))
e.add(78)
print(e)
s1={1,8,9}
s2={6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
s1={1,23,45}
s2={35,2,45,71}
s1-s2
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))
# True

print(B.issuperset(A))
# True

print(A.isdisjoint(B))
# False
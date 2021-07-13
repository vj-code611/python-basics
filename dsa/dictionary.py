#key-value pairs
#unordered
#mutable

myDict ={"name" : "Vijay", "age":21, "city":"Mysore"}
print(myDict)

myDict2=dict(name="Sampamth", age=21, city="Mysore")
print(myDict2)

#accessing value for a jey
value = myDict["name"]
print(value)

#Adding new key value
myDict["gender"] = "Male"
print(myDict)

#updating a value
myDict["city"] = "Bengaluru"
print(myDict)

#deleting a key value

#1.
del myDict["age"]
print(myDict)

#2.
#pop
myDict.pop("city")
print(myDict)

#3.
#popitem - remove last item
myDict.popitem()
print(myDict)


print("-----------------------")
print("#check any item present")
myDict ={"name" : "Vijay", "age":21, "city":"Mysore"}

print("--->#1. using If")
if "name" in myDict:
	print(myDict["name"])
else:
	print("not present")

if "name1" in myDict:
	print(myDict["name"])
else:
	print("not present")


print("--->#2. using try")
try:
	print(myDict("name"))
except:
	print("not present - error")



print("-----------------------")


print("\nitems():")
for i,j in myDict.items():
	print(i ,"-->", j )


print("\nkeys:")
for key in myDict:
	print(key)


print("\nkeys():")
for i in myDict.keys():
	print(i)


print("\nValues():")
for i in myDict.values():
	print(i)

print("-----------------------")
print("copying dict:\n")

myDict_cp = myDict
print(myDict_cp)

print("\nupdate org:")
myDict_cp["name"] ="Sampath"
print(myDict)
print(myDict_cp)

print("\nso use dict(ognlDict) to copy:")
myDict_cp1= dict(myDict)
myDict_cp1["name"] ="Ganesh"
print(myDict_cp1)
print(myDict)

print("-----------------------")
print("merge 2 dict:\n")

dic1= {"slno":1, "name":"Vijay"}
dic2= {"city":"Mysore", "skills":"hadoop"}

print("dic1:", dic1)
print("dic2:", dic2)

dic1.update(dic2)
print('dic1:',dic1)

print("-----------------------")
print("\ndict having tuple:\n")

mytuple=(2, 5)
mydic= {mytuple: 7}
print(mydic)

print("\ndict cant have list bz its mutable and hashable:\n")
mytuple=[2, 5]
# mydic= {mytuple: 7} #TypeError: unhashable type: 'list'

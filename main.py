# Create a dictionary
my_dict={
    "France": "Paris",
    "Netherlands": "Amsterdam",
     "Spain": "Madrid",
     "Italy": "Rome"
}
print(my_dict)

#Access value from my_dict
my_city=my_dict["Spain"]
print("I want to visit ",my_city )

#Create a list
flowers=["Rose","Tulip","sunflower"]
print(flowers)
#Access value from the list
print("i love  ",flowers[1])

#Get the list of keys
keys_list=list(my_dict.keys())
print(keys_list)

#Get the list of values
value_list=list(my_dict.values())
print(value_list)

#Loooping trough the keys and values of the dictonary
for key in my_dict:
    print(key)

for key in my_dict:
    print(my_dict[key])

#Adding a key value pier to the dictonary
my_dict["Turkey"]="Ankara"
print(my_dict)




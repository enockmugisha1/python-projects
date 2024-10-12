# Creating a hash map (dictionary) in Python

enock={}
# Define the put function
def put(dictionary, key, value):
    dictionary[key] = value

# Using the put function to add key-value pairs
put(enock, "enock", "football")
put(enock, "mugisha", "volleyball")
put(enock, "benon", "basketball")

# Print the dictionary
print(enock)

# Accessing values using keys
print("What they like:", enock["mugisha"])
print("What they like:", enock["benon"])

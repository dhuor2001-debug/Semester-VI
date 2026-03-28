#basic dictionary operation.
data= {"name":"Abraham",
       "age" : 20,
       "course": "CS",
       "nationality":"SSD"}
print(data)

#update a dictionary 
uodated_dict = {"name":"James",
                "age":27,
                "course":"CS",
                "nationality":"UG",
                "email":"james@gmail.com"}
data.update(uodated_dict)
print(f"updated dictionary: {data}")

#convert dictionary to list 
new_list = list(data.items())
print(f"List is here: {new_list}")

#clear the dictionary 
data.clear()
print(f"Empty dict: {data}")

#modified dictionary
data = {"name:":"PD",
        "tittle:":"professor",
        "Age":20,
        "nationality:":"India"}
print(f"modified dict:{data}")

data2 = {"name:":"Ch",
         "tittle":"professor",
         "Age":21,
         "nationality":"India"}

a = {**data,**data2}

print(f"merged Dict:{a}")


#frequency count
input_string = "student_data"
# Create a set of the string to count each unique character only once
unique_chars = set(input_string)

# Use dictionary comprehension to count the frequency of each unique character
frequency_dict = {char: input_string.count(char) for char in unique_chars}

# Print the result
print(frequency_dict)


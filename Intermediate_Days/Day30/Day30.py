###### File not found error:

# with open("Intermediate_Days\Day30\example_file.txt") as file:
#     file.read()
    
# Adding error handling:
# try:
#     file = open("Intermediate_Days\Day30\example_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     # print("There was an error")
#     file = open("Intermediate_Days\Day30\example_file.txt", "w")
# except KeyError as e:
#     print(f"Error: {e} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally: # Runs no matter what
#     file.close()
#     print("File was closed")
#     raise TypeError("This is a custom error")


### Raising an error:
height = float(input("Height: "))
weight = int(input("Weight: "))


if height > 3:
    raise ValueError("Human hieghts are not typically over 3 meters.")

bmi = weight / height ** 2
print(bmi)
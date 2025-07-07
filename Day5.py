# Loops
# Creating a password generator
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

print("Welcome to the Password Generator")

num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in you password?\n"))
num_symbols = int(input("How many symbokls would you like in your password?\n"))

pw = ""
for num in range(num_letters):
    pw += random.choice(letters)
for num in range(num_numbers):
    pw += random.choice(numbers)
for num in range(num_symbols):
    pw += random.choice(symbols)
print(pw)

pw = list(pw)
random.shuffle(pw)
pw = ''.join(pw)

print(f"Your password is: {pw}")
